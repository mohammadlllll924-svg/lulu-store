import hashlib
import os
import sys
import tempfile
import unittest
from io import BytesIO
from pathlib import Path

TEST_ROOT = Path(tempfile.mkdtemp(prefix="lulu-store-tests-"))
os.environ["DATABASE_PATH"] = str(TEST_ROOT / "store.db")
os.environ["PRIVATE_DOWNLOADS_DIR"] = str(TEST_ROOT / "private_downloads")
os.environ["SECRET_KEY"] = "test-only-secret-key"
os.environ["ADMIN_PASSWORD"] = "test-admin-password"
os.environ["SESSION_COOKIE_SECURE"] = "false"
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import app as store


class PrivateDownloadTests(unittest.TestCase):
    def setUp(self):
        store.PRIVATE_DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
        self.filename = f"test-{self._testMethodName}.pdf"
        (store.PRIVATE_DOWNLOADS_DIR / self.filename).write_bytes(b"%PDF-1.4\nprivate fixture\n")
        with store.app.app_context():
            db = store.get_db()
            db.execute("DELETE FROM orders")
            db.execute(
                "UPDATE products SET download_url = ?, payment_url = ? WHERE id = 1",
                (self.filename, "https://www.shopier.com/test"),
            )
            db.commit()
            self.product_id = 1
        self.client = store.app.test_client()

    def create_order(self, status="pending"):
        token = "unguessable-test-token-" + self._testMethodName
        token_hash = hashlib.sha256(token.encode("utf-8")).hexdigest()
        with store.app.app_context():
            db = store.get_db()
            cursor = db.execute(
                """INSERT INTO orders
                   (product_id, status, created_at, download_token_hash)
                   VALUES (?, ?, ?, ?)""",
                (self.product_id, status, "2026-01-01T00:00:00", token_hash),
            )
            db.commit()
            order_id = cursor.lastrowid
        return order_id, token

    def test_pending_order_is_not_downloadable(self):
        order_id, token = self.create_order("pending")
        response = self.client.get(f"/download/{order_id}?token={token}")
        self.assertEqual(response.status_code, 404)

        success = self.client.get(f"/success?order_id={order_id}&token={token}")
        self.assertEqual(success.status_code, 200)
        self.assertIn("الدفع قيد التحقق".encode(), success.data)
        self.assertNotIn("تحميل المنتج الآن".encode(), success.data)

    def test_paid_order_requires_the_order_token(self):
        order_id, token = self.create_order("paid")
        wrong = self.client.get(f"/download/{order_id}?token=wrong-token")
        self.assertEqual(wrong.status_code, 404)

        response = self.client.get(f"/download/{order_id}?token={token}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"%PDF-1.4\nprivate fixture\n")
        self.assertIn("attachment", response.headers.get("Content-Disposition", ""))
        self.assertIn("no-store", response.headers.get("Cache-Control", ""))
        response.close()

    def test_product_page_does_not_expose_a_file_url(self):
        response = self.client.get(f"/product/{self.product_id}")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"/static/downloads/", response.data)
        self.assertNotIn("تنزيل ملف المنتج PDF".encode(), response.data)

    def test_legacy_public_download_path_is_gone(self):
        response = self.client.get("/static/downloads/lulu-colors-letters-ar-tr.pdf")
        self.assertEqual(response.status_code, 404)

    def test_admin_upload_is_saved_under_an_internal_private_name(self):
        with self.client.session_transaction() as session:
            session["admin_logged_in"] = True
        response = self.client.post(
            "/admin/products/new",
            data={
                "title": "ملف اختبار خاص",
                "price": "1.00",
                "short_description": "اختبار",
                "description": "اختبار ملف خاص",
                "image_url": "",
                "payment_url": "https://www.shopier.com/test",
                "download_file": (BytesIO(b"%PDF-1.4\nprivate upload\n"), "secret-book.pdf"),
            },
            content_type="multipart/form-data",
        )
        self.assertEqual(response.status_code, 302)
        with store.app.app_context():
            product = store.get_db().execute(
                "SELECT download_url FROM products WHERE title = ?",
                ("ملف اختبار خاص",),
            ).fetchone()
        self.assertTrue(product["download_url"].endswith(".pdf"))
        self.assertNotEqual(product["download_url"], "secret-book.pdf")
        self.assertTrue((store.PRIVATE_DOWNLOADS_DIR / product["download_url"]).is_file())

    def test_only_admin_session_can_mark_an_order_paid(self):
        order_id, _token = self.create_order("pending")
        unauthenticated = self.client.post(
            f"/admin/orders/{order_id}/status", data={"status": "paid"}
        )
        self.assertEqual(unauthenticated.status_code, 302)
        with self.client.session_transaction() as session:
            session["admin_logged_in"] = True
        authorized = self.client.post(
            f"/admin/orders/{order_id}/status", data={"status": "paid"}
        )
        self.assertEqual(authorized.status_code, 302)
        with store.app.app_context():
            status = store.get_db().execute(
                "SELECT status FROM orders WHERE id = ?", (order_id,)
            ).fetchone()["status"]
        self.assertEqual(status, "paid")


if __name__ == "__main__":
    unittest.main()
