-- SQLite
-- Problema :
-- La tabla original presenta redundancia de datos, ya que repite información
-- de Customers, Phone, Address y products en varias filas.
-- Además, no permite manejar correctamente:
-- - Customers con múltiples Address
-- - Órdenes con varios products
/*
Order ID	Customer Name	Customer Phone	Address	    Item ID	Item Name	    Price	Quantity	Special Request	Delivery Time
001         Alice	        123-456-7890	123 Main St	101	    Cheeseburger	$8	    2	        No onions	    6:00 PM
001	        Alice	        123-456-7890	123 Main St	102	    Fries	        $3	    1	        Extra ketchup	6:00 PM
002	        Bob	            987-654-3210	456 Elm St	103	    Pizza	        $12	    1	        Extra cheese	7:30 PM
002	        Bob	            987-654-3210	456 Elm St	104	    Fries	        $3	    2	        None	        7:30 PM
003	        Claire	        555-123-4567	789 Oak St	105	    Salad	        $6	    1	        No croutons	    12:00 PM
004	        Claire	        555-123-4567	464 Georgia St	106	Water	        $1	    1	        None	        5:00 PM
------------------------------------------------------------------------------------------------------------------------------------
-- 1FN:
-- Se eliminan grupos repetitivos, cada fila representa un producto dentro de una orden.

-- 2FN:
-- Se separan los datos en tablas independientes según sus dependencias
-- Customer_Information, products, Address y Special_Request.

-- 3FN: Se eliminan dependencias transitivas, separando la información en tablas como Orders, Products
-- y Details_Order, asegurando que cada atributo dependa únicamente de su clave primaria.

--                       Orders                         |
|ID	        Customer_ID   Address_ID 	Delivery Time   |
|001             1	          1	    	   6:00 PM      |
|001	         1            1	           6:00 PM      |
|002	         2	          2	           7:30 PM      |
|002	         2	          2		       7:30 PM      |
|003	         3       	  3            12:00 PM     |
|004	         3            4	           5:00 PM      |

|        Customer_Information      |            Products                |         Special_Request         |              Address              
|Customer_ID Name	   Phone       |  ID	    Item Name	    Price	|  Request_ID	Request_Name      |  Address_ID	Customer_ID	Full_Address
|   1	     Alice	123-456-7890   |  1	       Cheeseburger	     $8	    |     1	          No Onion        |     1	         1	      123 Main St
|   2	     Bob	987-654-3210   |  2         Fries            $3     |     2	          Extra Ketchup   |     2	         2	      456 Elm St
|   3	     Claire	555-123-4567   |  3         Pizza            $12    |     3	          Extra Cheese    |     3	         3	      789 Oak St
|                                  |  4         Salad            $6     |     4	          No Croutons     |     4	         3	      464 Georgia St
|                                  |  5         Water            $1     |                                 |
|                                  |                                    |                                 |

------------------------------------------------------------------------------------------------------------------------------------
-- Aplicación de 2FN y diseño final:

-- Se crea la tabla Details_Order para representar la relación entre orders y products.
-- Esta tabla permite que:
-- Una orden tenga múltiples products
-- Un producto pueda estar en múltiples órdenes

|            ---tabla intermedia con claves foráneas
|                       Deteals_Order                     |               
|   ORDER_ID  Product_ID   Special_Request_ID	Quantity  |
|     001         1                1                2     |
|     001         2                2                1     |
|     002         3                3                1     |
|     002         2                NULL             2     |
|     003         4                4                1     |
|     004         5                NULL             1     |
|
-- La tabla Details_Order actúa como una tabla intermedia que resuelve
-- la relación muchos a muchos entre órdenes y productos, eliminando
-- redundancia y mejorando la integridad de los datos.  



-- cree la tabla principal de Orders, mas sencilla con solo cuatro columnas en vez de las diez que originalmente tenia

CREATE TABLE Orders (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_ID INTEGER REFERENCES Customer_Information(Customer_ID) NOT NULL,
    Address_ID INTEGER REFERENCES Address(Address_ID) NOT NULL,
    Delivery_time TEXT 
    );

-- creo la tabla de Orders para meter las ordenes mas explicadas, metiendo ahi ORDER_ID, Product_ID, Special_Request_ID y Quantity, evitando asi la repeticion de ordenes en la tabla principal
CREATE TABLE Deteals_Order (
    ORDER_ID INTEGER REFERENCES Orders(ID) NOT NULL,
    Product_ID INTEGER REFERENCES Products(Product_ID) NOT NULL,
    Special_Request_ID INTEGER REFERENCES Special_Request(Request_ID),
    Quantity INTEGER NOT NULL
    );
    

-- creo una tabla para almacenar ahi toda informacion personal de cada Customer, metiendo ahi las columnas Name y Phone
CREATE TABLE Customer_Information (
    Customer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(60) NOT NULL,
    Phone VARCHAR(40) DEFAULT(0)
    );

-- creo una tabla para almacenar ahi todos los productos y mas detalles como Name y Price
CREATE TABLE Products (
    Product_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Item_Name VARCHAR(40) NOT NULL,
    Price DECIMAL(10,2) DEFAULT(0)
    );

-- creo una tabla special solo para solicitudes speciales en ordenes
CREATE TABLE Special_Request (
    Request_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Request_Name VARCHAR(60) NOT NULL
    );

--creo una tabla para cuando los usuarios tengan mas de una direccion, como en el caso de Claire 
CREATE TABLE Address (
    Address_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Customer_ID INTEGER REFERENCES Customers(Customer_ID) NOT NULL,
    Full_Address VARCHAR(60) NOT NULL
    );
*/
INSERT INTO Customer_Information (Name, Phone)
    VALUES ('Alice', '123-456-7890'),
        ('Bob','987-654-3210'),
        ('Claire', '555-123-4567');

INSERT INTO Products (Item_Name, Price)
    VALUES ('Cheeseburger', 8),
        ('Fries', 3),
        ('Pizza', 12),
        ('Salad', 6),
        ('Water', 1);

INSERT INTO Special_Request (Request_Name)
    VALUES ('No Onion'),
        ('Extra Ketchup'),
        ('Extra Cheese'),
        ('No Croutons');

INSERT INTO Address (Customer_ID, Full_Address)
    VALUES (1, '123 Main St'),
        (2, '456 Elm St'),
        (3, '789 Oak St'),
        (3, '464 Georgia St');


INSERT INTO Deteals_Order (ORDER_ID, Product_ID, Special_Request_ID, Quantity)
    VALUES (001, 1, 1, 2),
        (001, 2, 2, 1),
        (002, 3, 3, 1),
        (002, 2, NULL,2),
        (003, 4, 4, 1),
        (004, 5, NULL,1);

INSERT INTO Orders (ID, Customer_ID, Address_ID, Delivery_time)
    VALUES (001, 1, 1, '6:00 PM'),
        (002, 2, 2, '7:30 PM'),
        (003, 3, 3, '12:00 PM'),
        (004, 3, 4, '5:00 PM');
