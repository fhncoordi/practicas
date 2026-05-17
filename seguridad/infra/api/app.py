"""
NebulaCorp — API REST de catálogo de productos (uso interno).
Versión 0.4-beta. Pendiente: revisar saneamiento de parámetros en /products.
"""
import os
from flask import Flask, request, jsonify, abort
import pymysql

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db-nebula")
DB_USER = os.environ.get("DB_USER", "appuser")
DB_PASS = os.environ.get("DB_PASS", "app_2024_pwd")
DB_NAME = os.environ.get("DB_NAME", "nebula")
API_KEY = os.environ.get("API_KEY", "changeme")


# FIXME(jdev): retirar este placeholder antes del primer release.
# Marcador histórico de cuando hardcodeábamos el token para los tests:
# HELICE{f1xm3_t3st_pl4c3h0ld3r_r3m0v3_b3f0r3}
def get_db():
    return pymysql.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor, autocommit=True,
    )


def require_api_key():
    key = request.headers.get("X-API-Key", "")
    if key != API_KEY:
        abort(401, description="X-API-Key inválida o ausente")


@app.route("/")
def root():
    return jsonify({
        "service": "NebulaCorp Internal API",
        "version": "0.4-beta",
        "endpoints": ["/health", "/products", "/products/<id>"],
        "auth": "Cabecera X-API-Key requerida en endpoints de datos",
    })


@app.route("/health")
def health():
    try:
        c = get_db()
        with c.cursor() as cur:
            cur.execute("SELECT 1")
        c.close()
        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


@app.route("/products")
def products():
    """
    Búsqueda libre de productos. Acepta el parámetro 'q' para filtrar por nombre
    o descripción. TODO(jdev): pasar a consulta parametrizada.
    """
    require_api_key()
    q = request.args.get("q", "")
    # ⚠ Vulnerable a SQL injection a propósito (didáctico)
    sql = "SELECT id, name, description, price FROM products " \
          "WHERE name LIKE '%" + q + "%' OR description LIKE '%" + q + "%'"
    try:
        c = get_db()
        with c.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
        c.close()
        return jsonify({"query": q, "count": len(rows), "results": rows})
    except pymysql.Error as e:
        # Devolvemos el error SQL crudo para facilitar el debug (oops)
        return jsonify({"error": str(e), "sql": sql}), 500


@app.route("/products/<int:pid>")
def product_detail(pid):
    require_api_key()
    c = get_db()
    with c.cursor() as cur:
        cur.execute("SELECT id, name, description, price FROM products WHERE id=%s", (pid,))
        row = cur.fetchone()
    c.close()
    if not row:
        abort(404)
    return jsonify(row)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
