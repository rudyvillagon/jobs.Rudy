--SQL
/*
CREATE TABLE Books (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(40),
    Author INTEGER REFERENCES Authors(ID)
    );

CREATE TABLE Authors (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(40)
    );

CREATE TABLE Customers (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(40),
    Email VARCHAR(60)
    );

CREATE TABLE Rents (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    BookID INTEGER REFERENCES Books(ID),
    CustomerID INTEGER REFERENCES Customers(ID),
    State VARCHAR(40)
    );

INSERT INTO Books(Name, Author)
    VALUES ('Don Quijote', 1),
        ('La Divina Comedia', 2),
        ('Vagabond 1-3', 3),
        ('Dragon Ball 1', 4),
        ('The Book of the 5 Rings', NULL);

INSERT INTO Authors (Name)
    VALUES ('Miguel de Cervantes'),
        ('Dante Alighieri'),
        ('Takehiko Inoue'),
        ('Akira Toriyama'),
        ('Walt Disney');

INSERT INTO Customers (Name, Email)
    VALUES ('John Doe', 'j.doe@email.com'),
        ('Jane Doe', 'jane@doe.com'),
        ('Luke Skywalker', 'darth.son@email.com');

INSERT INTO Rents (BookID ,CustomerID, State)
    VALUES (1, 2, 'Returned'),
        (2, 2, 'Returned'),
        (1, 1, 'On Time'),
        (3, 1, 'On Time'),
        (2, 2, 'Overdue');

*/

--Obtenga todos los libros y sus autores (en caso de tenerlos)
SELECT author.Name, Books.Name
FROM Authors AS author
INNER JOIN Books AS books
ON author.ID = books.Author;

--Obtenga todos los libros que no tienen autor
SELECT books.Name, books.Author
FROM Books AS books
LEFT JOIN Authors AS author 
ON  author.ID = books.Author
WHERE books.Author IS NULL;

--Obtenga todos los autores que no tienen libros
SELECT author.Name, books.Name
FROM Authors AS author
LEFT JOIN Books AS books 
ON  author.ID = books.Author
WHERE books.Author IS NULL;

--Obtenga todos los libros que han sido rentados en algún momento
SELECT books.Name, rents.BookID
FROM Books AS books
INNER JOIN Rents AS rents 
ON books.ID = rents.BookID; 

--Obtenga todos los libros que nunca han sido rentados
SELECT books.Name, rents.State
FROM Books AS books
LEFT JOIN Rents AS rents 
ON books.ID = rents.BookID
WHERE rents.BookID IS NULL;

--Obtenga todos los clientes que nunca han rentado un libro
SELECT customers.ID, customers.Name
FROM Customers AS customers
LEFT JOIN Rents AS rents 
ON customers.ID = rents.CustomerID
WHERE rents.State IS NULL;

--Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT books.Name, rents.State
FROM Books AS books
LEFT JOIN Rents AS rents 
ON rents.BookID = books.ID
WHERE rents.State IS 'Overdue';