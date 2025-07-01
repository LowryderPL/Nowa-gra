from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/api/inventory")
def get_inventory():
    conn = sqlite3.connect("firos_inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, type, rarity, description FROM inventory")
    rows = cursor.fetchall()
    conn.close()

    return jsonify([
        {"name": row[0], "type": row[1], "rarity": row[2], "description": row[3]}
        for row in rows
    ])

if __name__ == "__main__":
    app.run(debug=True)
