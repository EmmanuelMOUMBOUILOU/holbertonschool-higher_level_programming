from flask import Flask, request, render_template
import json
import csv
import os

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = []
    error = None

    try:
        if source == "json":
            if not os.path.exists("products.json"):
                raise FileNotFoundError("products.json not found")
            with open("products.json") as f:
                data = json.load(f)

        elif source == "csv":
            if not os.path.exists("products.csv"):
                raise FileNotFoundError("products.csv not found")
            with open("products.csv") as f:
                reader = csv.DictReader(f)
                data = list(reader)

        else:
            error = "Wrong source"
            data = []

        # If product_id is specified, filter the list
        if product_id:
            data = [item for item in data if str(item.get("id")) == str(product_id)]
            if not data:
                error = "Product not found"

    except Exception as e:
        error = str(e)
        data = []

    return render_template("product_display.html", products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
