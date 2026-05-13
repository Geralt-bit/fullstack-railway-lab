import os
import psycopg2
import psycopg2.extras
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL is not set")
    return psycopg2.connect(database_url, cursor_factory=psycopg2.extras.RealDictCursor)

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def index():
    return jsonify({"message": "Backend API is running", "student": "YOUR_NAME", "student_id": "YOUR_ID"})

@app.route("/api/data", methods=["GET"])
def get_data():
    init_db()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, created_at FROM tasks ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route("/api/data", methods=["POST"])
def add_data():
    init_db()
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "title is required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (%s) RETURNING id, title, created_at", (title,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(row), 201

@app.route("/api/data/<int:item_id>", methods=["DELETE"])
def delete_data(item_id):
    init_db()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s RETURNING id", (item_id,))
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if not deleted:
        return jsonify({"error": "not found"}), 404
    return jsonify({"message": "deleted", "id": item_id})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
