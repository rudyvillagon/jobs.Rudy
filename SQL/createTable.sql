-- SQLite

--Creo las tablas con sus columnas 
CREATE TABLE Users (
id INT PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(60) NOT NULL,
client_email VARCHAr(40) UNIQUE NOT NULL,
registration_data DATE NOT NULL
)

CREATE TABLE bill_products (
id INT PRIMARY KEY AUTOINCREMENT,
bill_number INT REFERENCES bills(id),
product_id INT REFERENCES products(id),
quantity INT NOT NULL,
total_amount DECIMAL(10,2) NOT NULL
)

CREATE TABLE bills (
id INT PRIMARY KEY AUTOINCREMENT,
user_full_name VARCHAR(60) REFERENCES Users(full_name),
purchase_date DATE NOT NULL,
client_email VARCHAR(40) REFERENCES Users(client_email),
payment_method_id INT REFERENCES payment_method(id),
total_amount DECIMAL(10,2) NOT NULL
)

CREATE TABLE cart_products (
id INT PRIMARY KEY AUTOINCREMENT,
id_shopping_cart INT REFERENCES shopping_cart(id),
product_id INT REFERENCES (id),
quantity INT NOT NULL
)

CREATE TABLE payment_method (
id INT PRIMARY KEY AUTOINCREMENT,
type_of_payment_method VARCHAR(30) NOT NULL,
name_bank VARCHAR(30)  NOT NULL
)

CREATE TABLE products (
id INT PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30) NOT NULL,
price DECIMAL(10,2) DEFAULT(0),
date DATE NOT NULL,
brand VARCHAR(20) NOT NULL
)

CREATE TABLE reviews (
id INT PRIMARY KEY AUTOINCREMENT,
user_id INT REFERENCES Users(id),
product_id INT REFERENCES products(id),
comment TEXT NOT NULL,
calification INTEGER CHECK (calification BETWEEN 1 AND 5),
date DATE NOT NULL
)

CREATE TABLE shopping_cart (
id INT PRIMARY KEY AUTOINCREMENT,
client_email VARCHAR(40) REFERENCES Users(client_email)
)

--Se agrega las nuevas columnas de numero de telefono de usuario y codigo de empleado a la tabla "Facturas"

ALTER TABLE bills 
    ADD user_phone INT(40) DEFAULT(0);

ALTER TABLE bills 
    ADD employee_cashier_code INT UNIQUE NOT NULL;
