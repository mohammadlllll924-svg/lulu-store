import hashlib
import os
import sqlite3
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

    def test_edition_copy_migration_preserves_custom_copy_and_delivery_settings(self):
        original_database = store.app.config["DATABASE"]
        with tempfile.TemporaryDirectory(prefix="lulu-copy-migration-") as tmp:
            database_path = Path(tmp) / "legacy.db"
            old_color_short = "كتاب PDF ثنائي اللغة عربي–تركي للأطفال من 3 إلى 6 سنوات، يجمع الحروف والأرقام والأشكال والحيوانات في أنشطة تلوين ممتعة."
            old_color_description = "كتاب PDF ثنائي اللغة من 9 صفحات من عالم لولو للصغار، يساعد الطفل على التعرف إلى الحروف العربية والتركية، بما فيها İ و I و Ş و Ğ و Ü و Ö و Ç، مع نطق عربي مبسّط للكلمات التركية عند الحاجة. يتضمن أنشطة للعدّ والتلوين واكتشاف الأشكال والتعرف إلى الحيوانات وتمارين التتبع والرسم، إضافة إلى شهادة إتمام تشجّع الطفل على مواصلة التعلم. مناسب للمنزل أو الروضة، ومصمم للأطفال من 3 إلى 6 سنوات."
            old_bear_description = "قصة قصيرة من 10 صفحات مناسبة للقراءة المشتركة. يتعلم الدب الصغير أن الشجاعة لا تعني غياب الخوف، بل التقدم خطوة وطلب المساندة عند الحاجة."
            with sqlite3.connect(database_path) as db:
                db.execute(
                    """CREATE TABLE products (
                        id INTEGER PRIMARY KEY, title TEXT NOT NULL,
                        short_description TEXT NOT NULL, description TEXT NOT NULL,
                        price TEXT NOT NULL, image_url TEXT NOT NULL,
                        payment_url TEXT NOT NULL, download_url TEXT NOT NULL,
                        created_at TEXT NOT NULL, updated_at TEXT NOT NULL)"""
                )
                db.execute(
                    """CREATE TABLE orders (
                        id INTEGER PRIMARY KEY, product_id INTEGER NOT NULL,
                        status TEXT NOT NULL, created_at TEXT NOT NULL)"""
                )
                db.execute(
                    """INSERT INTO products VALUES
                       (1, ?, ?, ?, '24.90', '', 'https://pay.example/color',
                        'keep-color.pdf', '2025-01-01', '2025-01-01')""",
                    ("ألوان وحروف مع لولو", old_color_short, old_color_description),
                )
                db.execute(
                    """INSERT INTO products VALUES
                       (2, ?, 'Admin teaser', ?, '14.90', '',
                        'https://pay.example/bear', 'keep-bear.pdf',
                        '2025-01-01', '2025-01-01')""",
                    ("الدب الصغير الشجاع", old_bear_description),
                )
            store.app.config["DATABASE"] = str(database_path)
            try:
                with store.app.app_context():
                    store.init_db()
                    rows = store.get_db().execute(
                        "SELECT * FROM products WHERE id IN (1, 2) ORDER BY id"
                    ).fetchall()
                color, bear = rows
                new_color = next(p for p in store.SEED_PRODUCTS if p["title"] == "ألوان وحروف مع لولو")
                new_bear = next(p for p in store.SEED_PRODUCTS if p["title"] == "الدب الصغير الشجاع")
                self.assertEqual(color["short_description"], new_color["short_description"])
                self.assertEqual(color["description"], new_color["description"])
                self.assertEqual(color["payment_url"], "https://pay.example/color")
                self.assertEqual(color["download_url"], "keep-color.pdf")
                self.assertEqual(bear["short_description"], "Admin teaser")
                self.assertEqual(bear["description"], new_bear["description"])
                self.assertEqual(bear["payment_url"], "https://pay.example/bear")
                self.assertEqual(bear["download_url"], "keep-bear.pdf")
            finally:
                store.app.config["DATABASE"] = original_database


if __name__ == "__main__":
    unittest.main()
