
-- SQLite
-- Problema :
-- Esta Tabla Tambien presenta redundancia de datos, ya que repite información
-- de Make, Phone, Address y se repite un automovil que tiene dos dueños diferentes.
-- y no permite manejar autos con multiples dueños
/*
VIN	        Make	    Model	Year	Color	OwnerID	OwnerName	OwnerPhone	    Insurance Company	Insurance Policy
1HGCM82633A	Honda	    Accord	2003	Silver	101 	Alice	    123-456-7890	ABC Insurance	    Fire & Theft
1HGCM82633A	Honda	    Accord	2003	Silver	102	    Bob	        987-654-3210	XYZ Insurance	    Full Cover
5J6RM4H79EL	Honda	    CR-V	2014	Blue	103	    Claire	    555-123-4567	DEF Insurance	    Collision
1G1RA6EH1FU	Chevrolet	Volt	2015	Red	    104	    Dave	    111-222-3333	GHI Insurance	    Basic Legal

--1FN:
--Se eliminan los grupos repetitivos, garantizando que cada fila contenga información de un único automóvil dentro de la lista.

-- 2FN:
-- Se separan los datos en tablas independientes según sus dependencias
-- Car_ID, Make, Owners y Insurance.

-- 3FN:
-- Se eliminan dependencias transitivas tambien, asi que cada categoria dependa
-- únicamente de su clave primaria.
|                       car_Information                    |
|     VIN        Make_ID   Model    Year    Color          |
|  1HGCM82633A      1      Accord   2003    Silver         |
|  1HGCM82633A      1      Accord   2003    Silver         |
|  5J6RM4H79EL      1      CR-V     2014    Blue           |
|  1G1RA6EH1FU      2      Volt     2015    Red            |
|                                                          |

|      Make         |             Owners                    |              Insurance                      |   
|   ID    Make      |   Owner_ID  Owner_Name  Owner_Phone   |  ID   Insurance_Company   Insurance_Policy  |
|    1    Honda     |     101       Alice     123-456-7890  |  1    ABC Insurance       Fire & Theft      |
|    2    Chvrolet  |     102       Bob       987-654-3210  |  2    XYZ Insurance       Full Cover        |
|                   |     103       Claire    555-123-4567  |  3    DEF Insurance       Collision         |
|                   |     104       Dave      111-222-3333  |  4    GHI Insurance       Basic Legal       |


--Creo estas tablas intermedias para que un carro pueda tener varios dueños y a su vez varios Seguros de Riesgos

|    Car_Owner           |    Car_Insurance         |
|   VIN        Owner_ID  |   VIN       Insurance_ID |
|1HGCM82633A    101      |1HGCM82633A       1       |
|1HGCM82633A    102      |1HGCM82633A       2       |
|5J6RM4H79EL    103      |5J6RM4H79EL       3       |
|1G1RA6EH1FU    104      |1G1RA6EH1FU       4       |






--cree esta tabla Car_ID para almacenar en ella todo lo que tenga que ver con el vehiculo VIN, Make, Model, Year, Color.
CREATE TABLE car_Information (
    VIN VARCHAR(40) PRIMARY KEY,
    Make_ID INTEGER REFERENCES Make(ID) NOT NULL,
    Model VARCHAR(40) NOT NULL,
    Year INTEGER NOT NULL, 
    Color VARCHAR(40) NOT NULL
    );

--cree una tabla Make para evitar repetir muchas veces una marca muy usada 
CREATE TABLE Make (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Make VARCHAR(40) NOT NULL
    );

--cree una tabla Owners para almacenar ahi la información de todos los dueños con Owner_Name y Owner_phone
CREATE TABLE Owners (
    Owner_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Owner_Name VARCHAR(40) NOT NULL,
    Owner_Phone VARCHAR(40) DEFAULT(0)
    );

--cree una tabla para todo lo que tiene que ver con el seguro de los vihiculos
CREATE TABLE Insurance (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Insurance_Company VARCHAR(40) NOT NULL,
    Insurance_Policy VARCHAR(40) NOT NULL
    );

CREATE TABLE Car_Insurance (
    VIN VARCHAR(40) REFERENCES car_Information(VIN) NOT NULL,
    Insurance_ID INTEGER REFERENCES Insurance(ID)
    );

CREATE TABLE Car_Owner (
    VIN VARCHAR(40) REFERENCES car_Information(VIN) NOT NULL,
    Owner_ID INTEGER REFERENCES Owners(Owner_ID) NOT NULL
    );
*/
INSERT INTO Make (Make)
    VALUES ('Honda'),
        ('Chevrolet');

INSERT INTO Owners (Owner_ID, Owner_Name, Owner_Phone)
    VALUES (101, 'Alice', '123-456-7890'),
        (102, 'Bob', '987-654-3210'),
        (103, 'Claire', '555-123-4567'),
        (104, 'Dave', '111-222-3333');

INSERT INTO Insurance (Insurance_Company, Insurance_Policy)
    VALUES ('ABC Insurance','Fire & Theft'),
        ('XYZ Insurance','Full Cover'),
        ('DEF Insurance','Collision'),
        ('GHI Insurance','Basic Legal');

INSERT INTO car_Information (VIN, Make_ID, Model, Year, Color)
    VALUES ('1HGCM82633A',1 ,'Accord','2003','Silver'),
        ('5J6RM4H79EL',1 ,'CR-V','2014','Blue'),
        ('1G1RA6EH1FU',2 ,'Volt','2015','Red');

--Tablas Intermedias
INSERT INTO Car_Owner (VIN, Owner_ID)
    VALUES ('1HGCM82633A', 101),
        ('1HGCM82633A', 102),
        ('5J6RM4H79EL', 103),
        ('1G1RA6EH1FU', 104);

INSERT INTO Car_Insurance (VIN, Insurance_ID)
    VALUES ('1HGCM82633A', 1),
        ('1HGCM82633A', 2),
        ('5J6RM4H79EL', 3),
        ('1G1RA6EH1FU', 4);
