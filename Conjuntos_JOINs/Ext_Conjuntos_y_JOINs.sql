--SQL


--1. La Operacion de All - Odd

--All = {1,2,3,4,5,6,7,8,9,10}
--Even = {2,4,6,8,10}
--Odd = {1,3,5,7,9}

-- La Opepacion de All - Odd, es tomar todos los elementos de All y quitarle todos los de Odd
-- en SQL esto seria un LEFT JOIN con un WHERE Odd.Num IS NULL

SELECT A.Num 
FROM AllNumbers AS A
LEFT JOIN OddNumbers AS Odd
ON A.Num = Odd.Num 
WHERE Odd.Num IS NULL;

--Esto simula una Resta

--2. Agrupamiento y conteo cruzado

SELECT Customers.Name,
        COUNT(Rents.ID) AS Total_rents
FROM Customers
INNER JOIN Rents
ON Customers.ID = Rents.CustomerID
GROUP BY Customers.Name
ORDER BY Total_Rents DESC
LIMIT 3;

--3. Consulta con múltiples JOINS anidados

SELECT Customers.Name AS Customer_Name,
    Books.Name AS Book_Name,
    Authors.Name AS Author_Name,
    Rents.State
FROM Rents
INNER JOIN Customers
ON Rents.ID = Customers.ID
INNER JOIN Books
ON Rents.BookID = Books.ID
LEFT JOIN Authors
ON Books.Aurhor = Authors.ID;