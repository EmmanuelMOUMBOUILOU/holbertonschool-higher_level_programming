from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_json_data():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception:
        return None

def load_csv_data():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            return [ 
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                } 
                for row in reader
            ]
    except Exception:
        return None

def load_sql_data(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id=?", (product_id,))
            row = cursor.fetchone()
            if row:
                return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]}]
            else:
                return []
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
    except Exception:
        return None
    finally:
        conn.close()

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error = None
    data = []

    if source == "json":
        data = load_json_data()
    elif source == "csv":
        data = load_csv_data()
    elif source == "sql":
        if id_param:
            try:
                data = load_sql_data(int(id_param))
                if not data:
                    error = "Product not found"
            except ValueError:
                error = "Invalid ID format"
                data = []
        else:
            data = load_sql_data()
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error, products=[])

    if data is None:
        error = "Failed to read data from source."
        data = []

    return render_template("product_display.html", products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
