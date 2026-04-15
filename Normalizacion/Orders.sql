-- SQLite
-- Los principales problemas de esta tabla es que tiene datos muy repetidos listas que se pueden poner en subtablas y agrupar mucha informacion que pertenece a una misma categoria, Usuarios con mas de una direccion y productos que se repiten en la lista.

/*Order ID	Customer Name	Customer Phone	Address	    Item ID	Item Name	    Price	Quantity	Special Request	Delivery Time
001         Alice	        123-456-7890	123 Main St	101	    Cheeseburger	$8	    2	        No onions	    6:00 PM
001	        Alice	        123-456-7890	123 Main St	102	    Fries	        $3	    1	        Extra ketchup	6:00 PM
002	        Bob	            987-654-3210	456 Elm St	103	    Pizza	        $12	    1	        Extra cheese	7:30 PM
002	        Bob	            987-654-3210	456 Elm St	104	    Fries	        $3	    2	        None	        7:30 PM
003	        Claire	        555-123-4567	789 Oak St	105	    Salad	        $6	    1	        No croutons	    12:00 PM
004	        Claire	        555-123-4567	464 Georgia St	106	Water	        $1	    1	        None	        5:00 PM
*/
-- cree la tabla principal de Orders, mas sencilla con solo cuatro columnas en vez de las diez que originalmente tenia
CREATE TABLE Orders (
    Deteals_Order INTEGER REFERENCES Deteals_Order(Deteal_ID) NOT NULL,
    Customer_ID INTEGER REFERENCES Customers(Customer_ID) NOT NULL,
    Address_ID INTEGER REFERENCES Address(Address_ID) NOT NULL,
    Delivery_time TEXT 
    );

-- creo la tabla de Orders para meter las ordenes mas explicadas, metiendo ahi Product_ID, Special_Request_ID y Quantity, evitando asi la repeticion de ordenes en la tabla principal
CREATE TABLE Deteals_Order (
    Deteal_ID INTEGER NOT NULL,
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


INSERT INTO Deteals_Order (Deteal_ID, Product_ID, Special_Request_ID, Quantity)
    VALUES (001, 1, 1, 2),
        (001, 2, 2, 3),
        (002, 3, 3, 12),
        (002, 2, NULL,3),
        (003, 4, 4, 6),
        (004, 5, NULL,1);

INSERT INTO Orders (Deteals_Order, Customer_ID, Address_ID, Delivery_time)
    VALUES (001, 1, 1, '6:00 PM'),
        (002, 2, 2, '7:30 PM'),
        (003, 3, 3, '12:00 PM'),
        (004, 3, 4, '5:00 PM');
