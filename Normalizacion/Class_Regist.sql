--SQL
/*
--El problema con esta tabla es la reiteración de datos como Students, Course Name y tambien la informacion del 
-- los datos del Instructor como nombres y correos, cuenta con columnas que se podrian manejar 
-- unicamente con los PKs


|Student ID	Student Name	Course Code	Course Name	Instructor Name	Instructor Email  |
|   301	        Marco Gómez	    CS101	    Python I	Juan Pérez	    juan@uni.edu  |
|   301	        Marco Gómez	    CS102	    Python II	Laura Rojas	    laura@uni.edu |
|   302	        Carla Ruiz	    CS101	    Python I	Juan Pérez	    juan@uni.edu  |

--FN1: Elimino los Grupos repetidos, cada linea representa los un Student, Course y Instructor.

--FN2: Se Separan los datos en tablas independientes segun su dependencia en Student, Course y Instructor.

--FN3: Se eliminan la dependecias trancitivas, separando los datos en tablas como Class_regist y Course
--asegurando que cada atributo dependa de una PKs

|      Students      ||                Courses                   ||             Instructors                 ||
| ID   Student_name  || Course_Code  Course_Name  Instructor_ID  ||  ID  Instructor_Name  Instructor_Email  ||
|301   Marco Gómez   ||  CS101        Python I         401       || 401  Juan Pérez       juan@uni.edu      ||
|302   Carla Ruiz    ||  CS102        Python II        402       || 402  Laura Rojas      laura@uni.edu     ||
|                    ||                                          ||                                         ||

--Creo la tabla Class_regist para que represente la relacion entre las tres tablas anteriores Stundents, Courses y Instructors
--permitiendo asi que un Estudiante pueda estar en varios curso y que hayan distintos cursos con multiples instructores.

|           Class_regist            |
|   Student_ID        Course_Code   | 
|      301              CS101       |
|      301              CS102       |
|      302              CS101       |
|                                   |
|                                   |
|                                   |

-- La Tabla Class_Regist acutia como intermediaria entre los muchos Estudiantes que pueden haber asi como los 
-- diferentes cursos y sus respectivos Intructores, eliminando asi las redundancias asi como y asi mejorar la 
-- comprencion de los datos.
*/

CREATE TABLE Students (
    ID INTEGER PRIMARY KEY NOT NULL,
    Student_name VARCHAR(40) NOT NULL
    );

CREATE TABLE Courses (
    Course_Code VARCHAR(10) PRIMARY KEY NOT NULL,
    Course_Name VARCHAR(40) NOT NULL,
    Instructor_ID INTEGER REFERENCES Instructors(ID) NOT NULL
    );

CREATE TABLE Instructors (
    ID INTEGER PRIMARY KEY NOT NULL,
    Instructor_Name VARCHAR(40) NOT NULL,
    Instructor_Email VARCHAR(40) NOT NULL
    );

CREATE TABLE Class_regist (
    Student_ID INTEGER REFERENCES Student(ID) NOT NULL,
    Course_Code VARCHAR(10) REFERENCES Courses(Course_Code) NOT NULL
    );

INSERT INTO Students (ID, Student_name)
    VALUES (301, 'Marco Gómez'),
        (302, 'Carla Ruiz');

INSERT INTO Instructors (ID, Instructor_Name, Instructor_Email)
    VALUES (401, 'Juan Pérez', 'juan@uni.edu'),
        (402, 'Laura Rojas', 'laura@uni.edu');

INSERT INTO Courses (Course_Code, Course_Name, Instructor_ID)
    VALUES ('CS101', 'Python I', 401),
        ('CS102', 'Python II', 402);

INSERT INTO Class_regist (Student_ID, Course_Code)
    VALUES (301, 'CS101'),
        (301, 'CS102'),
        (302, 'CS101');

