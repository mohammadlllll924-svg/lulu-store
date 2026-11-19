import os
import secrets
import sqlite3
from datetime import datetime
from functools import wraps
from pathlib import Path

from dotenv import load_dotenv
from flask import (
    Flask, abort, flash, g, redirect, render_template, request,
    session, url_for
)

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATABASE = Path(os.getenv("DATABASE_PATH", BASE_DIR / "store.db"))
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(32))

app = Flask(__name__)
app.config.update(
    SECRET_KEY=SECRET_KEY,
    DATABASE=str(DATABASE),
    MAX_CONTENT_LENGTH=2 * 1024 * 1024,
)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            short_description TEXT NOT NULL DEFAULT '',
            description TEXT NOT NULL DEFAULT '',
            price TEXT NOT NULL DEFAULT '0',
            image_url TEXT NOT NULL DEFAULT '',
            payment_url TEXT NOT NULL DEFAULT '',
            download_url TEXT NOT NULL DEFAULT '',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TEXT NOT NULL,
            FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE CASCADE
        );
        """
    )
    db.commit()


def admin_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not ADMIN_PASSWORD:
            return render_template("admin.html", setup_required=True), 503
        if not session.get("admin_logged_in"):
            return redirect(url_for("admin_login", next=request.path))
        return view(*args, **kwargs)
    return wrapped_view


@app.context_processor
def inject_globals():
    return {"store_name": os.getenv("STORE_NAME", "متجري الرقمي")}


@app.route("/")
def index():
    products = get_db().execute(
        "SELECT * FROM products ORDER BY id DESC"
    ).fetchall()
    return render_template("index.html", products=products)


@app.route("/product/<int:product_id>")
def product(product_id):
    item = get_db().execute(
        "SELECT * FROM products WHERE id = ?", (product_id,)
    ).fetchone()
    if item is None:
        abort(404)
    return render_template("product.html", product=item)


@app.route("/checkout/<int:product_id>", methods=["GET", "POST"])
def checkout(product_id):
    item = get_db().execute(
        "SELECT * FROM products WHERE id = ?", (product_id,)
    ).fetchone()
    if item is None:
        abort(404)
    if not item["payment_url"]:
        flash("رابط الدفع لهذا المنتج غير متاح حالياً. يرجى المحاولة لاحقاً.", "error")
        return redirect(url_for("product", product_id=product_id))

    db = get_db()
    cursor = db.execute(
        "INSERT INTO orders (product_id, status, created_at) VALUES (?, ?, ?)",
        (product_id, "pending", datetime.utcnow().isoformat(timespec="seconds")),
    )
    db.commit()
    success_url = url_for("success", product_id=product_id, _external=True)
    separator = "&" if "?" in item["payment_url"] else "?"
    payment_url = f"{item['payment_url']}{separator}order_id={cursor.lastrowid}&success_url={success_url}"
    return redirect(payment_url)


@app.route("/success/<int:product_id>")
@app.route("/success")
def success(product_id=None):
    if product_id is None:
        product_id = request.args.get("product_id", type=int)
    item = None
    if product_id:
        item = get_db().execute(
            "SELECT * FROM products WHERE id = ?", (product_id,)
        ).fetchone()
    if item is None:
        return render_template("success.html", product=None), 404
    return render_template("success.html", product=item)


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if not ADMIN_PASSWORD:
        return render_template("admin.html", setup_required=True), 503
    if request.method == "POST":
        if secrets.compare_digest(request.form.get("password", ""), ADMIN_PASSWORD):
            session.clear()
            session["admin_logged_in"] = True
            return redirect(request.args.get("next") or url_for("admin"))
        flash("كلمة المرور غير صحيحة.", "error")
    return render_template("admin.html", login=True)


@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/admin")
@admin_required
def admin():
    products = get_db().execute("SELECT * FROM products ORDER BY id DESC").fetchall()
    orders = get_db().execute(
        """SELECT orders.*, products.title AS product_title
           FROM orders JOIN products ON products.id = orders.product_id
           ORDER BY orders.id DESC LIMIT 50"""
    ).fetchall()
    return render_template("admin.html", products=products, orders=orders)


def product_form_values():
    return {
        "title": request.form.get("title", "").strip(),
        "short_description": request.form.get("short_description", "").strip(),
        "description": request.form.get("description", "").strip(),
        "price": request.form.get("price", "").strip(),
        "image_url": request.form.get("image_url", "").strip(),
        "payment_url": request.form.get("payment_url", "").strip(),
        "download_url": request.form.get("download_url", "").strip(),
    }


@app.route("/admin/products/new", methods=["GET", "POST"])
@admin_required
def add_product():
    if request.method == "POST":
        data = product_form_values()
        if not data["title"] or not data["price"]:
            flash("العنوان والسعر حقول مطلوبة.", "error")
            return render_template("admin.html", form_product=data, form_mode="new")
        now = datetime.utcnow().isoformat(timespec="seconds")
        db = get_db()
        db.execute(
            """INSERT INTO products
               (title, short_description, description, price, image_url,
                payment_url, download_url, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (*data.values(), now, now),
        )
        db.commit()
        flash("تمت إضافة المنتج بنجاح.", "success")
        return redirect(url_for("admin"))
    return render_template("admin.html", form_product=None, form_mode="new")


@app.route("/admin/products/<int:product_id>/edit", methods=["GET", "POST"])
@admin_required
def edit_product(product_id):
    db = get_db()
    item = db.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
    if item is None:
        abort(404)
    if request.method == "POST":
        data = product_form_values()
        if not data["title"] or not data["price"]:
            flash("العنوان والسعر حقول مطلوبة.", "error")
            return render_template("admin.html", form_product=data, form_mode="edit")
        db.execute(
            """UPDATE products SET title=?, short_description=?, description=?,
               price=?, image_url=?, payment_url=?, download_url=?, updated_at=?
               WHERE id=?""",
            (*data.values(), datetime.utcnow().isoformat(timespec="seconds"), product_id),
        )
        db.commit()
        flash("تم تحديث المنتج.", "success")
        return redirect(url_for("admin"))
    return render_template("admin.html", form_product=item, form_mode="edit")


@app.post("/admin/products/<int:product_id>/delete")
@admin_required
def delete_product(product_id):
    db = get_db()
    db.execute("DELETE FROM products WHERE id = ?", (product_id,))
    db.commit()
    flash("تم حذف المنتج.", "success")
    return redirect(url_for("admin"))


@app.post("/admin/orders/<int:order_id>/status")
@admin_required
def update_order_status(order_id):
    status = request.form.get("status", "pending")
    if status not in {"pending", "paid", "cancelled"}:
        abort(400)
    db = get_db()
    db.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
    db.commit()
    return redirect(url_for("admin"))


with app.app_context():
    init_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
