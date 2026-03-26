-- SQLite
/*
--Creo la tabla categorias con las columnas id, name, description.
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40) NOT NULL,
    description VARCHAR(60) UNIQUE NOT NULL
    );

--Agrego columna "category_id" a "Products"
ALTER TABLE products
    ADD category_id;

--Agrego 3 filas en categorias 
INSERT INTO categories (name, description)
    VALUES ('Hombres', 'Ropa para Hombres');

INSERT INTO categories (name, description)
    VALUES ('Mujeres', 'Ropa para Mujeres');

INSERT INTO categories (name, description)
    VALUES ('Niños', 'Ropa para Niños');

--Actualice los productos ya en stock con la nueva columna "category_id"
UPDATE products SET
    category_id = 1
    WHERE id = 1;

UPDATE products SET
    category_id = 1
    WHERE id = 2;

UPDATE products SET
    category_id = 2
    WHERE id = 3;

UPDATE products SET
    category_id = 2
    WHERE id = 4;

UPDATE products SET
    category_id = 3
    WHERE id = 5;

UPDATE products SET
    category_id = 3
    WHERE id = 6;

--Filtro los products que muestren (id, product_name, price, category_id)
SELECT id, product_name, price, category_id
    FROM products;

--2. inserte 10 filas nuevas en products 
INSERT INTO products (name, price, date, brand, category_id)
    VALUES('Socks',7500 ,'2014-11-03' ,'Vans' ,1 ),
        ('Sweater',50000 ,'2010-02-03' ,'Addidas' ,2 ),
        ('swimsuit',25000 ,'2024-01-02' ,'Speedo' ,3 ),
        ('T-Shirt',60000 ,'2023-10-23' ,'Polo' ,3 ),
        ('Shoes',90000 ,'2011-12-30' ,'Boss' ,1 ),
        ('Coat',100000 ,'2010-09-18' ,'Columbia' ,2 ),
        ('Hat',27000 ,'2002-12-01' ,'Old Navy' ,1 ),
        ('Pants',35000 ,'2015-03-08' ,'Levis' ,2 ),
        ('Glasses',140000 ,'2005-11-15' ,'Oakley' ,1 ),
        ('Short',30000 ,'2020-06-02' ,'GAP' ,3 );

--Seleciono todos los products
SELECT *
    FROM products

-- Seleccione los products con price > 50000
SELECT *
    FROM products
    WHERE price > 50000

--Seleccione los products con la palabra "apple" usando Like
SELECT * 
    FROM products
    WHERE name LIKE 'apple';

--Seleccione los 5 products mas caros
SELECT *
    FROM products
    ORDER By price DESC
    LIMIT 5;
*/    

