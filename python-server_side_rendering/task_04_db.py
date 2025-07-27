from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')  # <-- Add this
    data = []
    error = None

    try:
        if source == "json":
            with open("products.json", "r") as f:
                all_products = json.load(f)
                if product_id:
                    data = [p for p in all_products if str(p["id"]) == str(product_id)]
                else:
                    data = all_products

        elif source == "csv":
            with open("products.csv", newline='') as f:
                reader = csv.DictReader(f)
                if product_id:
                    data = [row for row in reader if row["id"] == str(product_id)]
                else:
                    data = list(reader)

        elif source == "sql":
            if not os.path.exists("products.db"):
                raise FileNotFoundError("Database not found.")
            conn = sqlite3.connect("products.db")
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            if product_id:
                cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
            else:
                cursor.execute("SELECT * FROM Products")

            rows = cursor.fetchall()
            data = [dict(row) for row in rows]
            conn.close()
        else:
            error = "Wrong source"
    except Exception as e:
        error = f"Error loading data: {e}"

    return render_template("product_display.html", products=data, error=error)


# Optional: single product lookup
@app.route('/products/<int:product_id>')
def product_by_id(product_id):
    source = request.args.get('source')
    product = None
    error = None

    try:
        if source == "sql":
            conn = sqlite3.connect("products.db")
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products WHERE id=?", (product_id,))
            row = cursor.fetchone()
            if row:
                product = dict(row)
            conn.close()
        elif source == "json":
            with open("products.json", "r") as f:
                all_products = json.load(f)
                for item in all_products:
                    if int(item["id"]) == product_id:
                        product = item
                        break
        elif source == "csv":
            with open("products.csv", newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if int(row["id"]) == product_id:
                        product = row
                        break
        else:
            error = "Wrong source"
    except Exception as e:
        error = f"Error retrieving product: {e}"

    return render_template("product_display.html", products=[product] if product else [], error=error)

if __name__ == '__main__':
    app.run(debug=True)
