import hashlib
import os
import secrets
import sqlite3
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from dotenv import load_dotenv
from flask import (
    Flask, abort, flash, g, redirect, render_template, request,
    send_from_directory, session, url_for,
)
from werkzeug.utils import secure_filename

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATABASE = Path(os.getenv("DATABASE_PATH", BASE_DIR / "store.db"))
PRIVATE_DOWNLOADS_DIR = Path(
    os.getenv("PRIVATE_DOWNLOADS_DIR", BASE_DIR / "private_downloads")
).resolve()
DATABASE.parent.mkdir(parents=True, exist_ok=True)
PRIVATE_DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_hex(32)
MAX_UPLOAD_BYTES = 25 * 1024 * 1024

SHOPIER_LULU_BOOK_PAYMENT_URL = os.getenv(
    "SHOPIER_LULU_BOOK_PAYMENT_URL",
    "",
)
SEED_PRODUCTS = [
    {
        "title": "ألوان وحروف مع لولو",
        "short_description": "طبعة 2026 ثنائية اللغة عربي–تركي من 11 صفحة، تجمع الحروف والألوان والأرقام والأشكال والحيوانات في أنشطة ممتعة.",
        "description": "طبعة 2026 من كتاب PDF ثنائي اللغة من 11 صفحة من عالم لولو للصغار، تساعد الطفل على التعرف إلى الحروف العربية والتركية، بما فيها İ و I و Ş و Ğ و Ü و Ö و Ç، مع نطق عربي مبسّط للكلمات التركية عند الحاجة. تتضمن أنشطة للألوان والعدّ والأشكال والحيوانات وتمارين تتبع ورسم، إضافة إلى شهادة إتمام. مناسبة للمنزل أو الروضة، ومصممة للأطفال من 3 إلى 6 سنوات.",
        "price": "24.90",
        "image_url": "",
        "payment_url": SHOPIER_LULU_BOOK_PAYMENT_URL,
        "download_url": "lulu-colors-letters-ar-tr.pdf",
    },
    {
        "title": "مغامرات لولو — كتاب التلوين",
        "short_description": "طبعة 2026 من 28 صفحة: 25 صفحة تلوين أصلية، مع غلاف ودليل استخدام وصفحة رسم إضافية.",
        "description": "طبعة 2026 من كتاب مغامرات لولو تضم 28 صفحة إجمالًا: غلافًا، ودليلًا موجزًا للاستخدام، و25 صفحة التلوين الأصلية، وصفحة أخيرة يرسم فيها الطفل مغامرته الجديدة. مناسبة للمنزل أو الروضة، وتشجع الخيال واللعب الهادئ.",
        "price": "17.90",
        "image_url": "/static/images/lulu-adventures.jpg",
        "payment_url": "",
        "download_url": "lulu-adventures-coloring-pages.pdf",
    },
    {
        "title": "حزمة أوراق العمل الأولى مع لولو",
        "short_description": "طبعة 2026 من 12 صفحة للتتبع والعدّ والأنماط والمقارنة والمهارات المبكرة.",
        "description": "حزمة تعليمية من 12 صفحة، تختلف عن كتب التلوين والقصص: تركز على مهارات ما قبل الكتابة، والعدّ، والأنماط، والمقارنة والانتباه من خلال أنشطة عملية بسيطة للأطفال في المنزل أو الروضة.",
        "price": "15.90",
        "image_url": "/static/images/lulu-worksheets.jpg",
        "payment_url": "",
        "download_url": "lulu-preschool-worksheets.pdf",
    },
    {
        "title": "بطاقات لولو المصورة: عربي–تركي–إنجليزي",
        "short_description": "طبعة 2026 من 12 صفحة تضم 20 بطاقة مفردات مصورة بالعربية والتركية والإنجليزية.",
        "description": "بطاقات مفردات متعددة اللغات من 12 صفحة تضم 20 بطاقة مصورة، تجمع العربية والتركية والإنجليزية في نشاط واحد. صممت للمراجعة الشفوية واللعب مع أحد أفراد العائلة، وليست كتاب تلوين أو قصة.",
        "price": "12.90",
        "image_url": "/static/images/lulu-flashcards.jpg",
        "payment_url": "",
        "download_url": "lulu-trilingual-flashcards.pdf",
    },
    {
        "title": "الدب الصغير الشجاع",
        "short_description": "طبعة 2026 من 13 صفحة بثلاث لغات عن الشجاعة الهادئة وطلب المساعدة ومشاركة المشاعر.",
        "description": "قصة قصيرة من 13 صفحة مناسبة للقراءة المشتركة، تسرد الحكاية نفسها بالعربية والتركية والإنجليزية، مع صفحة ختامية للنقاش والرسم. يتعلم الدب الصغير أن الشجاعة لا تعني غياب الخوف، بل التفكير بهدوء وطلب المساندة بأمان عند الحاجة.",
        "price": "14.90",
        "image_url": "/static/images/lulu-brave-bear.jpg",
        "payment_url": "",
        "download_url": "lulu-brave-little-bear.pdf",
    },
    {
        "title": "مغامرات لولو: الأرقام | Lulu'nun Maceraları: Sayılar",
        "short_description": "كتاب PDF ثنائي اللغة عربي–تركي للأطفال من 3 إلى 6 سنوات لتعلّم الأرقام والعد والأنماط والمسائل البسيطة بطريقة مرحة.",
        "description": "كتاب أنشطة ثنائي اللغة من 7 صفحات يعرّف الطفل بالأرقام العربية وأسمائها التركية مع نطق عربي مبسّط، ويقدّم تدريبات العد والتعرّف إلى الأنماط ومسائل الجمع والرسم. مناسب للمنزل والروضة، بصيغة PDF وأسلوب تلويني ممتع للأطفال من 3 إلى 6 سنوات.",
        "price": "299.90",
        "image_url": "",
        "payment_url": os.getenv("SHOPIER_LULU_NUMBERS_PAYMENT_URL", ""),
        "download_url": "",
    },
    {
        "title": "مغامرات لولو: الألوان والأشكال | Lulu'nun Maceraları: Renkler ve Şekiller",
        "short_description": "كتاب PDF ثنائي اللغة عربي–تركي لاكتشاف الألوان والأشكال من خلال التلوين والبحث والرسم.",
        "description": "كتاب أنشطة ثنائي اللغة من 7 صفحات يساعد الأطفال من 3 إلى 6 سنوات على تعلّم الألوان والأشكال بالعربية والتركية، مع أنشطة توصيل ولعبة بحث وتمارين رسم وتلوين. يتضمن الكلمات التركية الأساسية بنطق عربي مبسّط عند الحاجة، وهو مناسب للمنزل أو الروضة.",
        "price": "289.90",
        "image_url": "",
        "payment_url": os.getenv("SHOPIER_LULU_COLORS_PAYMENT_URL", ""),
        "download_url": "",
    },
    {
        "title": "مغامرات لولو: الحيوانات والكلمات | Lulu'nun Maceraları: Hayvanlar ve Kelimeler",
        "short_description": "كتاب PDF ثنائي اللغة عربي–تركي يتعرّف فيه الطفل إلى الحيوانات وكلماتها وبيئاتها من خلال التلوين والرسم.",
        "description": "كتاب أنشطة ثنائي اللغة من 7 صفحات يعرّف الأطفال من 3 إلى 6 سنوات بالحيوانات وأسمائها بالعربية والتركية، مع نطق عربي مبسّط للكلمات التركية. يتضمن أنشطة مطابقة الحيوان ببيئته وطعامه، وصفحة للرسم وقصة صغيرة لتنمية اللغة والخيال.",
        "price": "299.90",
        "image_url": "",
        "payment_url": os.getenv("SHOPIER_LULU_ANIMALS_PAYMENT_URL", ""),
        "download_url": "",
    },
]

app = Flask(__name__)
app.config.update(
    SECRET_KEY=SECRET_KEY,
    DATABASE=str(DATABASE),
    MAX_CONTENT_LENGTH=MAX_UPLOAD_BYTES,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.getenv(
        "SESSION_COOKIE_SECURE", "true" if os.getenv("RENDER") else "false"
    ).lower() == "true",
)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def normalize_private_filename(value):
    """Accept only a PDF basename; never treat a stored value as a public URL."""
    if not value:
        return ""
    raw_name = Path(urlsplit(str(value).strip()).path).name
    safe_name = secure_filename(raw_name)
    if not safe_name or Path(safe_name).suffix.lower() != ".pdf":
        return ""
    return safe_name


def private_file_exists(filename):
    safe_name = normalize_private_filename(filename)
    if not safe_name:
        return False
    candidate = (PRIVATE_DOWNLOADS_DIR / safe_name).resolve()
    return candidate.parent == PRIVATE_DOWNLOADS_DIR and candidate.is_file()


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
            download_token_hash TEXT NOT NULL DEFAULT '',
            FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE CASCADE
        );
        """
    )

    # Safe, in-place migration for existing Render SQLite databases.
    order_columns = {
        row[1] for row in db.execute("PRAGMA table_info(orders)").fetchall()
    }
    if "download_token_hash" not in order_columns:
        db.execute(
            "ALTER TABLE orders ADD COLUMN download_token_hash TEXT NOT NULL DEFAULT ''"
        )

    # Convert legacy public URLs to private basenames. External URLs are discarded.
    for row in db.execute("SELECT id, download_url FROM products").fetchall():
        old_value = row["download_url"] or ""
        if old_value.startswith("/static/downloads/"):
            new_value = normalize_private_filename(old_value)
        elif old_value.startswith("http://") or old_value.startswith("https://"):
            new_value = ""
        else:
            new_value = normalize_private_filename(old_value)
        if new_value != old_value:
            db.execute(
                "UPDATE products SET download_url = ? WHERE id = ?",
                (new_value, row["id"]),
            )

    now = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec="seconds")
    for product in SEED_PRODUCTS:
        exists = db.execute(
            "SELECT 1 FROM products WHERE title = ? LIMIT 1",
            (product["title"],),
        ).fetchone()
        if exists is None:
            db.execute(
                """INSERT INTO products
                   (title, short_description, description, price, image_url,
                    payment_url, download_url, created_at, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    product["title"], product["short_description"],
                    product["description"], product["price"],
                    product["image_url"], product["payment_url"],
                    product["download_url"], now, now,
                ),
            )
        # Existing rows are intentionally left unchanged here so administrator
        # edits and uploaded private-file names survive restarts and deployments.

    # Update only the known previous stock descriptions; customized admin copy
    # is preserved field-by-field, and payment/file settings are never touched.
    legacy_copy = {
        "ألوان وحروف مع لولو": {
            "short_description": "كتاب PDF ثنائي اللغة عربي–تركي للأطفال من 3 إلى 6 سنوات، يجمع الحروف والأرقام والأشكال والحيوانات في أنشطة تلوين ممتعة.",
            "description": "كتاب PDF ثنائي اللغة من 9 صفحات من عالم لولو للصغار، يساعد الطفل على التعرف إلى الحروف العربية والتركية، بما فيها İ و I و Ş و Ğ و Ü و Ö و Ç، مع نطق عربي مبسّط للكلمات التركية عند الحاجة. يتضمن أنشطة للعدّ والتلوين واكتشاف الأشكال والتعرف إلى الحيوانات وتمارين التتبع والرسم، إضافة إلى شهادة إتمام تشجّع الطفل على مواصلة التعلم. مناسب للمنزل أو الروضة، ومصمم للأطفال من 3 إلى 6 سنوات.",
        },
        "مغامرات لولو — كتاب التلوين": {
            "short_description": "كتاب تلوين من 25 صفحة برسومات لطيفة تشجع الطفل على الخيال والتركيز واللعب الهادئ.",
            "description": "رحلة تلوين من 25 صفحة مع لولو، مناسبة للأطفال في المنزل أو الروضة. كل صفحة تمنح الطفل مساحة للتلوين والتخيل دون تكرار فكرة المنتجات الأخرى.",
        },
        "حزمة أوراق العمل الأولى مع لولو": {
            "short_description": "نسخة مركزة من 10 صفحات للتتبع والعدّ والمطابقة والمهارات المبكرة، للاستخدام السريع في البيت أو الروضة.",
            "description": "حزمة تعليمية قصيرة من 10 صفحات، تختلف عن كتب التلوين والقصص: تركز على مهارات ما قبل الكتابة، العدّ، المطابقة والانتباه من خلال أنشطة عملية بسيطة.",
        },
        "بطاقات لولو المصورة: عربي–تركي–إنجليزي": {
            "short_description": "8 صفحات من المفردات المصورة بثلاث لغات لمساعدة الطفل على ربط الصورة بالكلمة بطريقة مرحة.",
            "description": "بطاقات مفردات متعددة اللغات من 8 صفحات، تجمع العربية والتركية والإنجليزية في نشاط واحد. صممت للمراجعة الشفوية واللعب مع أحد أفراد العائلة، وليست كتاب تلوين أو قصة.",
        },
        "الدب الصغير الشجاع": {
            "short_description": "قصة مصورة من 10 صفحات عن الشجاعة الهادئة وطلب المساعدة ومشاركة المشاعر.",
            "description": "قصة قصيرة من 10 صفحات مناسبة للقراءة المشتركة. يتعلم الدب الصغير أن الشجاعة لا تعني غياب الخوف، بل التقدم خطوة وطلب المساندة عند الحاجة.",
        },
    }
    seed_by_title = {product["title"]: product for product in SEED_PRODUCTS}
    for title, previous_copy in legacy_copy.items():
        row = db.execute(
            "SELECT id, short_description, description FROM products WHERE title = ?",
            (title,),
        ).fetchone()
        if row is None:
            continue
        changed = {
            field: seed_by_title[title][field]
            for field, old_value in previous_copy.items()
            if row[field] == old_value
        }
        if changed:
            assignments = ", ".join(f"{field} = ?" for field in changed)
            db.execute(
                f"UPDATE products SET {assignments}, updated_at = ? WHERE id = ?",
                (*changed.values(), now, row["id"]),
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


@app.after_request
def add_security_headers(response):
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    if request.endpoint in {"success", "download_order"}:
        response.headers["Cache-Control"] = "private, no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    return response


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
    return render_template(
        "product.html", product=item,
        download_ready=private_file_exists(item["download_url"]),
    )


def append_query_params(url, params):
    parsed = urlsplit(url)
    query = dict(parse_qsl(parsed.query, keep_blank_values=True))
    query.update(params)
    return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urlencode(query), parsed.fragment))


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
    if not private_file_exists(item["download_url"]):
        flash("ملف المنتج غير جاهز للتسليم بعد؛ لم يتم بدء عملية الدفع.", "error")
        return redirect(url_for("product", product_id=product_id))

    token = secrets.token_urlsafe(32)
    db = get_db()
    cursor = db.execute(
        """INSERT INTO orders
           (product_id, status, created_at, download_token_hash)
           VALUES (?, ?, ?, ?)""",
        (
            product_id,
            "pending",
            datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec="seconds"),
            hashlib.sha256(token.encode("utf-8")).hexdigest(),
        ),
    )
    db.commit()
    order_id = cursor.lastrowid
    success_url = url_for(
        "success", order_id=order_id, token=token, _external=True
    )
    payment_url = append_query_params(
        item["payment_url"],
        {"order_id": order_id, "success_url": success_url},
    )
    return redirect(payment_url)


@app.route("/success")
def success():
    order_id = request.args.get("order_id", type=int)
    token = request.args.get("token", "")
    if not order_id or not token:
        return render_template(
            "success.html", product=None, order_status="unverified",
            download_url=None,
        ), 400

    order = get_db().execute(
        """SELECT orders.id, orders.status, orders.download_token_hash,
                  products.id AS product_id, products.title, products.download_url
           FROM orders JOIN products ON products.id = orders.product_id
           WHERE orders.id = ?""",
        (order_id,),
    ).fetchone()
    if order is None or not order["download_token_hash"]:
        abort(404)
    token_hash = hashlib.sha256(token.encode("utf-8")).hexdigest()
    if not secrets.compare_digest(order["download_token_hash"], token_hash):
        abort(404)

    download_url = None
    if order["status"] == "paid" and private_file_exists(order["download_url"]):
        download_url = url_for(
            "download_order", order_id=order_id, token=token
        )
    return render_template(
        "success.html", product=order, order_status=order["status"],
        download_url=download_url,
    )


@app.route("/download/<int:order_id>")
def download_order(order_id):
    token = request.args.get("token", "")
    order = get_db().execute(
        """SELECT orders.status, orders.download_token_hash,
                  products.title, products.download_url
           FROM orders JOIN products ON products.id = orders.product_id
           WHERE orders.id = ?""",
        (order_id,),
    ).fetchone()
    if order is None or order["status"] != "paid" or not order["download_token_hash"]:
        abort(404)

    supplied_hash = hashlib.sha256(token.encode("utf-8")).hexdigest()
    if not secrets.compare_digest(order["download_token_hash"], supplied_hash):
        abort(404)

    filename = normalize_private_filename(order["download_url"])
    if not filename or not private_file_exists(filename):
        abort(404)
    download_name = secure_filename(order["title"]) or "digital-product"
    return send_from_directory(
        str(PRIVATE_DOWNLOADS_DIR), filename,
        as_attachment=True,
        download_name=f"{download_name}.pdf",
        mimetype="application/pdf",
        max_age=0,
        conditional=False,
    )


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
    db = get_db()
    products = db.execute("SELECT * FROM products ORDER BY id DESC").fetchall()
    file_ready_by_id = {
        product["id"]: private_file_exists(product["download_url"])
        for product in products
    }
    orders = db.execute(
        """SELECT orders.*, products.title AS product_title
           FROM orders JOIN products ON products.id = orders.product_id
           ORDER BY orders.id DESC LIMIT 50"""
    ).fetchall()
    return render_template(
        "admin.html", products=products, orders=orders,
        file_ready_by_id=file_ready_by_id,
    )


def product_form_values():
    return {
        "title": request.form.get("title", "").strip(),
        "short_description": request.form.get("short_description", "").strip(),
        "description": request.form.get("description", "").strip(),
        "price": request.form.get("price", "").strip(),
        "image_url": request.form.get("image_url", "").strip(),
        "payment_url": request.form.get("payment_url", "").strip(),
    }


def store_uploaded_pdf():
    uploaded = request.files.get("download_file")
    if uploaded is None or not uploaded.filename:
        return ""
    original_name = secure_filename(uploaded.filename)
    if not original_name or Path(original_name).suffix.lower() != ".pdf":
        raise ValueError("ارفع ملفاً بصيغة PDF فقط.")
    if uploaded.mimetype not in {"application/pdf", "application/octet-stream"}:
        raise ValueError("نوع الملف غير صالح؛ المطلوب ملف PDF.")
    header = uploaded.stream.read(5)
    uploaded.stream.seek(0)
    if header != b"%PDF-":
        raise ValueError("الملف لا يبدو ملف PDF صالحاً.")
    stored_name = f"{secrets.token_hex(16)}.pdf"
    uploaded.save(PRIVATE_DOWNLOADS_DIR / stored_name)
    return stored_name


@app.route("/admin/products/new", methods=["GET", "POST"])
@admin_required
def add_product():
    if request.method == "POST":
        data = product_form_values()
        if not data["title"] or not data["price"]:
            flash("العنوان والسعر حقول مطلوبة.", "error")
            return render_template("admin.html", form_product=data, form_mode="new"), 400
        try:
            data["download_url"] = store_uploaded_pdf()
        except ValueError as error:
            flash(str(error), "error")
            return render_template("admin.html", form_product=data, form_mode="new"), 400
        now = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec="seconds")
        db = get_db()
        db.execute(
            """INSERT INTO products
               (title, short_description, description, price, image_url,
                payment_url, download_url, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (*data.values(), now, now),
        )
        db.commit()
        flash("تمت إضافة المنتج. حُفظ ملف PDF في مساحة خاصة غير قابلة للوصول المباشر.", "success")
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
            return render_template(
                "admin.html", form_product=data, form_mode="edit",
                current_file_ready=private_file_exists(item["download_url"]),
            ), 400
        try:
            new_file = store_uploaded_pdf()
        except ValueError as error:
            flash(str(error), "error")
            return render_template(
                "admin.html", form_product=data, form_mode="edit",
                current_file_ready=private_file_exists(item["download_url"]),
            ), 400
        data["download_url"] = new_file or item["download_url"]
        db.execute(
            """UPDATE products SET title=?, short_description=?, description=?,
               price=?, image_url=?, payment_url=?, download_url=?, updated_at=?
               WHERE id=?""",
            (*data.values(), datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec="seconds"), product_id),
        )
        db.commit()
        flash("تم تحديث المنتج. رابط التسليم يظل محمياً ولا يظهر في صفحة المنتج.", "success")
        return redirect(url_for("admin"))
    return render_template(
        "admin.html", form_product=item, form_mode="edit",
        current_file_ready=private_file_exists(item["download_url"]),
    )


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
    result = db.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
    if result.rowcount == 0:
        abort(404)
    db.commit()
    if status == "paid":
        flash("سُجل الطلب كمدفوع. لا تفعل ذلك إلا بعد التحقق من الدفع في لوحة Shopier.", "success")
    else:
        flash("تم تحديث حالة الطلب.", "success")
    return redirect(url_for("admin"))


with app.app_context():
    init_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
