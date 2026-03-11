-- SQLite

--Obtenga todos los productos almacenados
SELECT *
    FROM products;

--Obtenga todos los productos que tengan un precio mayor a 50000
SELECT *
    FROM products
    WHERE price > 50000;

--Obtenga todas las compras de un mismo producto por id.
SELECT *
    FROM bill_products
    WHERE product_id = 1;

--Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT product_id, SUM(quantity) as total_amount
    FROM bill_products
    GROUP by product_id;

--Obtenga todas las facturas realizadas por el mismo comprador
SELECT *
    FROM bills
    WHERE full_name = 'Juan Castro Jimenes';

--Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT *
    FROM bills
    ORDER by total_amount DESC

--Obtenga una sola factura por número de factura.
SELECT DISTINCT bill_number
    FROM bill_products;