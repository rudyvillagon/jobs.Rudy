
--Products
--Users
--Bills

CREATE TABLE Products (
    ID VARCHAR(40) PRIMARY KEY,
    Name VARCHAR(40) NOT NULL,
    Price DECIMAL(10,2) DEFAULT(0),
    Inventory INTEGER DEFAULT(0)
);

CREATE TABLE Users (
    ID VARCHAR(40) PRIMARY KEY,
    Name VARCHAR(60) NOT NULL
);

CREATE TABLE Bills (
    ID VARCHAR(40) PRIMARY KEY,
    User_ID VARCHAR(40) REFERENCES Users(ID) NOT NULL,
    Bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Bill_Details (
    ID VARCHAR(40) PRIMARY KEY,
    Bill_ID VARCHAR(40) REFERENCES Bills(ID) NOT NULL,
    Product_ID VARCHAR(40) REFERENCES Products(ID) NOT NULL,
    Quantity INTEGER NOT NULL Check (Quantity > 0),
    Unit_Price DECIMAL(10,2) NOT NULL
);

INSERT INTO Products (ID, Name, Price, Inventory)
    VALUES ('P001', 'PEPSI', 2, 14),
        ('P002', 'COCA COLA', 2.5, 20),
        ('P003', 'FANTA', 1, 30),
        ('P004', 'SPRIT', 1, 27),
        ('P005', 'CANADA DRY', 2.5, 37);

INSERT INTO Users (ID, Name)
    VALUES ('U001', 'Pedro Alfaro'),
        ('U002', 'Carmen Rojas'),
        ('U003', 'Marco Sandoval'),
        ('U004', 'Jimena Salas'),
        ('U005', 'Juan Sancho');

INSERT INTO Bills (ID, User_ID)
    VALUES ('B001', 'U002'),
        ('B002', 'U004'),
        ('B003', 'U002'),
        ('B004', 'U003'),
        ('B005', 'U001');

INSERT INTO Bill_Details (ID, Bill_ID, Product_ID, Quantity, Unit_Price)
    VALUES ('D001', 'B001', 'P004', 2, 1),
        ('D002', 'B002', 'P005', 1, 2.5),
        ('D003', 'B003', 'P001', 4, 2),
        ('D004', 'B004', 'P003', 2, 1),
        ('D005', 'B005', 'P004', 3, 1);

----------------------------------------------------------------------

--Esto lo hice para el Ejercicio 3

ALTER TABLE Bills
ADD COLUMN Status VARCHAR(40);

UPDATE Bills
SET Status = 'Delivered'
WHERE ID = 'B001';

UPDATE Bills
SET Status = 'Delivered'
WHERE ID = 'B002';

UPDATE Bills
SET Status = 'Delivered'
WHERE ID = 'B003';

UPDATE Bills
SET Status = 'Delivered'
WHERE ID = 'B004';

UPDATE Bills
SET Status = 'Delivered'
WHERE ID = 'B005';