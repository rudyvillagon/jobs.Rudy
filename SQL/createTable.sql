-- SQLite
-- SQLite

--Creo las tablas con sus columnas 
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(60) NOT NULL,
    client_email VARCHAR(40) UNIQUE NOT NULL,
    registration_data DATE NOT NULL
    );

CREATE TABLE bill_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_number INTEGER REFERENCES bills(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL
    );

CREATE TABLE bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id_name INTEGER REFERENCES Users(id),
    purchase_date DATE NOT NULL,
    payment_method_id INTEGER REFERENCES payment_method(id),
    total_amount DECIMAL(10,2) NOT NULL
    );

CREATE TABLE cart_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_shopping_cart INTEGER REFERENCES shopping_cart(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL
    );

CREATE TABLE payment_method (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_of_payment_method VARCHAR(30) NOT NULL,
    name_bank VARCHAR(30)  NOT NULL
    );

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    price DECIMAL(10,2) DEFAULT(0),
    date DATE NOT NULL,
    brand VARCHAR(20) NOT NULL
    );

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES Users(id),
    product_id INTEGER REFERENCES products(id),
    comment TEXT NOT NULL,
    calification INTEGER CHECK (calification BETWEEN 1 AND 5),
    date DATE NOT NULL
    );

CREATE TABLE shopping_cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_email VARCHAR(40) REFERENCES Users(client_email)
    );

--Se agrega las nuevas columnas de numero de telefono de usuario y codigo de empleado a la tabla "Facturas"

ALTER TABLE bills 
    ADD user_phone VARCHAR(40) DEFAULT(0);

ALTER TABLE bills 
    ADD employee_cashier_code INTEGER NOT NULL DEFAULT(0);






