--SQL
/*
--Problema: La tabla presenta repeticion de datos como empleados, depatamentos y numeros de telefono. Cuenta con varias columnas que podrian separarce y utilizarse con solo una PK, asi 
--hacer mas facil el manejo de datos y evitar errores.

--|--Employee ID	Employee Name	Department	Department Phone	Project ID	Project Name	Project Budget  |
--|    201	        Ana Rivera	        IT	    2222-2222	        P001	    Web App	            50000       |
--|    201	        Ana Rivera	        IT	    2222-2222	        P002	    API REST	        25000       |
--|    202	        Luis Mendez	     Marketing	1111-1111	        P003	    TV Campaign	        30000       |

--1FN:
--Se Eliminan los grupos repetidos, cada linea representa un empleado y un proyecto.

--2FN: 
-- se separan los datos en tablas independientes segun su dependencias
-- Employees, Departments y projects

--3FN:
--Se Eliminan dependencias transitivas, asi que cada categoria dependa de un PK


--separo todos los datos en tres tablas 
--              Employees                               Departments_Information                       Project_Information
| Employee_ID  Employee_name  Department_ID  |  ID  Department  Department_phone   | Project_ID  Project_name Project_Budget   |
|     201       Ana Rivera          1        |  1        IT             2222-2222       |  P001         Web App        50000        |
|     202       Luis Mendez         2        |  2     Marketing         1111-1111       |  P002         API REST       25000        |
|                                            |                                          |  P003        TV Campaign     30000        |
|                                            |                                          |                                           |

--quedando la tabla asi abierta a cambios de empleados nuevos y reaciognacion a nuevos departameentos hasta el punto de que pueda cambiar el  
---tabla intermedia con claves foráneas
---   Control_Projects
| Employee_ID  Project_ID  |
|   201            P001    |
|   201            P002    |
|   202            P003    |
|                          | 

*/
CREATE TABLE Control_Projects (
    Employee_ID INTEGER REFERENCES  Employees(Employee_ID) NOT NULL,
    Project_ID VARCHAR(10) REFERENCES Project_Information(Project_ID) NOT NULL
    );

CREATE TABLE Employees (
    Employee_ID  INTEGER PRIMARY KEY NOT NULL,
    Employee_name VARCHAR(40) NOT NULL,
    Department_ID INTETER REFERENCES Department_Name(ID)
    );

CREATE TABLE Departments_Information (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Department VARCHAR(40) NOT NULL,
    Department_Phone VARCHAR(40) NOT NULL
    );

CREATE TABLE Project_Information (
    Project_ID VARCHAR(20) PRIMARY KEY NOT NULL,
    Project_name VARCHAR(60) NOT NULL,
    Project_Budget DECIMAL(10,2) DEFAULT(0)
    );

INSERT INTO Control_Projects (Employee_ID, Project_ID)
    VALUES(201, 'P001'),
        (201, 'P002'),
        (202, 'P003');

INSERT INTO Employees (Employee_ID, Employee_name, Department_ID)
    VALUES(201, 'Ana Riverav', 1),
        (202, 'Luis Mendez', 2);

INSERT INTO Departments_Information (Department, Department_Phone)
    VALUES('IT', '2222-2222'),
        ('Marketing', '1111-1111');

INSERT INTO Project_Information (Project_ID, Project_name, Project_Budget)
    VALUES('P001', 'Web App', 50000),
        ('P002', 'API REST', 25000),
        ('P003', 'TV Campaign', 30000);
