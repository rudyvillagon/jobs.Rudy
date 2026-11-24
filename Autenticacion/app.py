from flask import Flask


from routes_fruits_management import fruit_routes
from routes_invoices_management import invoices_routes
from autentification import users_veri

app = Flask("fruit-shop")

app.register_blueprint(fruit_routes)
app.register_blueprint(invoices_routes)
app.register_blueprint(users_veri)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

