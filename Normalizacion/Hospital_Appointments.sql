--SQL
/*
--Los Problemas de esta tabla es que tiene muchas reiteraciones de datos de Patients y Doctors, tambien con columnas que
--se podrian agrupar en tablas segun sus relaciones y manejarse con una sola PK

|Appointment ID	Patient Name	Patient Phone	Doctor Name	    Specialty	Date	    Time        |
|A01	        Diana Vargas	8888-1111	    Dr. Soto	    Pediatría	2024-08-01	10:00 AM    |
|A02	        Diana Vargas	8888-1111	    Dr. Soto	    Pediatría	2024-08-10	10:00 AM    |
|A03	        Edwin Mora	    8999-2222	    Dr. Mora	    Cardiología	2024-08-05	01:00 PM    |

--1FN:
--Se eliminan los grupos repetitivos, garantizando que cada fila contenga información de una unica cita en el Hospital dentro de la lista.

-- 2FN:
-- Se separan los datos en tablas independientes según sus dependencias
-- Hospital_Appointments, Patients, Doctors y Specialty.

-- 3FN:
-- Se eliminan dependencias transitivas tambien, asi que cada cita del Hospital dependa
-- únicamente de su PK.

|            Patients                 ||           Doctors            ||          Specialty          |
| ID     Patient_Name  Patient_Phone  || ID   Doctor_Name   Specialty || ID     Specialty_Name       |
| P001   Diana Vargas  8888-1111      || D01  Dr. Soto      S001      || S001   Pediatría            |
| P002   Edwin Mora    8999-2222      || D02  Dr. Mora      S002      || S002   Cardiología          |
|                                     ||                              ||                             |
|                                     ||                              ||                             |

--Creo una tabla intermedia donde una paciente pueda tener varias citas 
--y donde una Doctor pueda tener varios pacientes agendados

--                     ---tabla intermedia con claves foráneas
|                            Hospital_Appointments                                    |     
| Appointment_ID         Patient_ID        Doctor_ID     Date               Time      |
|      A01                  P001              D01        2024-08-01         10:00 AM  |
|      A02                  P001              D01        2024-08-10         10:00 AM  |
|      A03                  P002              D02        2024-08-05         01:00 PM  |
|                                                                                     |
| 
*/                                                                                    |
CREATE TABLE Patients (
    ID VARCHAR(10) PRIMARY KEY,
    Patient_Name VARCHAR(40) NOT NULL,
    Patient_Phone VARCHAR(30) NOT NULL
    );

CREATE TABLE Doctors (
    ID VARCHAR(10) PRIMARY KEY,
    Doctor_Name VARCHAR(40) NOT NULL,
    Specialty VARHCAR(10) NOT NULL
    );
CREATE TABLE Specialty (
    ID VARHCAR(10) PRIMARY KEY,
    Specialty_Name VARCHAR(40) NOT NULL
    );

CREATE TABLE Hospital_Appointments (
    Appointment_ID VARCHAR(10) PRIMARY KEY,
    Patient_ID VARCHAR(10) REFERENCES Patients(ID) NOT NULL,
    Doctor_ID VARCHAR(10) REFERENCES Doctors(ID) NOT NULL,
    Date DATE NOT NULL,
    Time TEXT NOT NULL
    );

INSERT INTO Patients (ID, Patient_Name, Patient_Phone)
    VALUES ('P001', 'Diana Vargas', '8888-1111'),
        ('P002', 'Edwin Mora', '8999-2222');

INSERT INTO Doctors (ID, Doctor_Name, Specialty)
    VALUES ('D01', 'Dr. Soto', 'S001'),
        ('D02', 'Dr. Mora', 'S002');

INSERT INTO Specialty (ID, Specialty_Name)
    VALUES ('S001', 'Pediatría'),
        ('S002', 'Cardiología');

INSERT INTO Hospital_Appointments (Appointment_ID, Patient_ID, Doctor_ID, Date, Time)
    VALUES ('A01', 'P001', 'D01', '2024-08-01', '10:00 AM'),
        ('A02', 'P001', 'D01', '2024-08-10', '10:00 AM'),
        ('A03', 'P002', 'D02', '2024-08-05', '01:00 PM');