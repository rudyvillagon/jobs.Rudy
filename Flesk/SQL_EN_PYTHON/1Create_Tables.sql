--SQL

CREATE SCHEMA lyfter_car_rental;


CREATE TABLE lyfter_car_rental.User_status (
    id SERIAL PRIMARY KEY,
    user_status_mode VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE lyfter_car_rental.Brands_cars (
    id SERIAL PRIMARY KEY,
    brand_name VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE lyfter_car_rental.Cars_status (
    id SERIAL PRIMARY KEY,
    cars_status_mode VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE lyfter_car_rental.Rent_status (
    id SERIAL PRIMARY KEY,
    rent_status_mode VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE lyfter_car_rental.Users (
    id SERIAL PRIMARY KEY,
    user_fullname VARCHAR(60) NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL,
    user_name VARCHAR(40) UNIQUE NOT NULL,
    password VARCHAR(40) NOT NULL,
    date_birth DATE NOT NULL,
    user_status INTEGER REFERENCES lyfter_car_rental.User_status(id)
);

CREATE TABLE lyfter_car_rental.Cars (
    id SERIAL PRIMARY KEY,
    brand INTEGER REFERENCES lyfter_car_rental.Brands_cars(id),
    model VARCHAR(40) NOT NULL,
    fabrication_year INTEGER NOT NULL,
    car_status INTEGER REFERENCES lyfter_car_rental.Cars_status(id)
);

CREATE TABLE lyfter_car_rental.Rentals (
	id SERIAL PRIMARY KEY,
    user_ID INTEGER REFERENCES lyfter_car_rental.Users(id),
    car_ID INTEGER REFERENCES lyfter_car_rental.Cars(id),
    rent_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rental_status INTEGER REFERENCES lyfter_car_rental.Rent_status(id)
);

INSERT INTO lyfter_car_rental.User_status(user_status_mode)
    VALUES ('Active'),
        ('Inactive'),
        ('Suspended'),
        ('Pending'),
		('Defaulter')

INSERT INTO lyfter_car_rental.Brands_cars(brand_name)
    VALUES ('Ford'),
    ('Mazda'),
    ('Suzuki'),
    ('Porsche'),
    ('Toyota'),
    ('Nissan'),
    ('Kia'),
    ('Jeep'),
    ('BMW'),
    ('Mitsubishi')

INSERT INTO lyfter_car_rental.Cars_status(cars_status_mode)
	VALUES ('Available'),
	('Rented'),
	('Reserved'),
	('Maintenance'),
	('Cleaning'),
	('Out of Service'),
	('Damaged'),
	('Retired')

INSERT INTO lyfter_car_rental.Rent_status (rent_status_mode)
	VALUES ('Pending'),
	('Confirmed'),
	('Active'),
	('Completed'),
	('Cancelled'),
	('Overdue')

INSERT INTO lyfter_car_rental.Users(user_fullname, email, user_name, password, date_birth, user_status)
    VALUES 		(
			'Jackie Ritchie Sr.',		
			'Caleb_Ullrich1@yahoo.com',		
			'Jeanne_Welch',		
			'JqBE_8NB53wHtRy',		
			'1981-02-24',
            1		
    ),
		(
			'Dr. Rickey Heidenreich-Daniel',		
			'William_Hoeger20@gmail.com',		
			'Kaelyn_Reilly-Blick96',		
			'VMNTvXIRkjXgulh',		
			'2004-02-18',
            1		
        ),
		(
			'Joann Boehm',		
			'Rick_Mraz59@yahoo.com',		
			'Theresa13',		
			'G4nf4h9TJ5kaRE_',		
			'2007-08-20',
            1		
		),
		(
			'Loretta Ziemann MD',		
			'Charlotte.Lynch26@hotmail.com',		
			'Lilian47',		
			'2avVjTwJO469Mtn',		
			'2002-10-10',
            2		
		),
		(
			'Ray Konopelski',		
			'Bennie_Carroll45@yahoo.com',		
			'Hattie99',		
			'9mqCE7iL11jCtDb',		
			'1985-07-09',
            1		
		),
		(
			'Vivian Effertz',		
			'Glenda.Grady81@yahoo.com',		
			'Johan_Kerluke',		
			'NQDoKC1sSIYWbvo',		
			'1992-01-07',
            3		
		),
		(
			'Barry DAmore DDS',		
			'Jenna.Stracke@gmail.com',		
			'Eleanore_Fisher',		
			'4ej62U8KHuB6TYD',		
			'1979-08-08',
            1		
		),
		(
			'Kim Simonis',		
			'Kendra_MacGyver@yahoo.com',		
			'Moshe.Murazik',		
			'ea2f90KPaq_V2cy',		
			'1984-03-18',
            2		
		),
		(
			'Harry Olson',		
			'Rosie.Heidenreich18@gmail.com',		
			'Jermaine.Kozey',		
			'GagX4Tw71lBkeeb',		
			'2008-05-17',
            4		
		),
		(
			'Ida Smitham',		
			'Terrance_Jacobi31@gmail.com',		
			'Billy_Gislason78',		
			'a5AHf53iopRvrGd',		
			'1979-04-11',
            1		
		),
		(
			'Jeffrey Sawayn II',		
			'Josefina_King@gmail.com',		
			'Ruth.Senger-Kuhic98',		
			'wdOoZ96FPizYbmu',		
			'1981-05-04',
            1		
		),
		(
			'Winston Greenfelder',		
			'Chris_Braun@hotmail.com',		
			'Kristian26',		
			'RH_xFJgOOfc4HXS',		
			'1998-02-11',
            1		
		),
		(
			'Casey Batz',		
			'Sammy_Weber-Johnson@hotmail.com',		
			'Giovanni_Parker',		
			'uEDVXpuaobrhlOY',		
			'2000-11-23',
            2		
		),
		(
			'Jennie Dare',		
			'Sarah.Kshlerin@yahoo.com',		
			'Merlin.Hauck',		
			'swB1O2dfR_GhQHH',		
			'1980-01-01',
            1		
		),
		(
			'Jeffrey Hermiston V',		
			'Lynn_Collins84@gmail.com',		
			'Romaine80',		
			'BsbNsBq1UN49u40',		
			'1989-03-05',
            1		
		),
		(
			'Christopher Hoeger',		
			'Louise.Franecki-Bruen@gmail.com',		
			'Jovany_Mohr2',		
			'DgnfuMNxv2o5oax',		
			'1995-08-06',
            2		
		),
		(
			'Omar Schinner',		
			'Lauren_Vandervort-Price@yahoo.com',		
			'Rozella65',		
			'5bBbK7iksnLIv41',		
			'1977-04-12',
            1		
		),
		(
			'Mrs. Sophie Bartoletti',		
			'Gene.Schinner70@yahoo.com',		
			'Harmony.Cremin55',		
			'kJzQSJUTMhj2hEL',		
			'1989-06-18',
            1		
		),
		(
			'Courtney Zieme',		
			'Earl_Wyman29@gmail.com',		
			'Nico.Walter43',		
			'_0NaL6aNLSiWlYb',		
			'1975-04-25',
            2		
		),
		(
			'Dr. Darla Conn',		
			'Alfredo_Jenkins75@gmail.com',		
			'Nils.Roberts82',		
			'02SxSK0kZLMfvcu',		
			'2008-06-01',
            3		
		),
		(
			'Claire Renner',		
			'Tonya.Thompson48@yahoo.com',		
			'Jaiden_Hodkiewicz89',		
			'jFdmOB0OKVTQmB0',		
			'1989-03-19',
            1		
		),
		(
			'Bridget Emard-Rippin',		
			'Opal_Blanda@yahoo.com',		
			'Stefanie.Bartoletti2',		
			'Yda2E_9Gdbbr1dv',		
			'1978-06-10',
            4		
		),
		(
			'Dr. Sergio Nader-Luettgen',		
			'Salvatore.Hettinger@yahoo.com',		
			'Jody.Beahan',		
			'phgmKH1Jy8VrLk2',		
			'1999-06-19',
            1		
		),
		(
			'Darryl Barrows',		
			'Kirk.McLaughlin15@hotmail.com',		
			'Aliza.Schultz',		
			'rWvnbgsK6dnNH5s',		
			'1996-11-27',
            1		
		),
		(
			'Cathy Kulas',		
			'Sheldon_Collier@gmail.com',		
			'Isai.Jenkins44',		
			'XKdvV5EfD3yZ_Rp',		
			'1987-05-25',
            2		
		),
		(
			'Francis Roob II',		
			'Terry_Bashirian-Stracke@gmail.com',		
			'Phyllis42',		
			'5CTbPb3v26_QIsJ',		
			'2003-11-21',
            1		
		),
		(
			'Bob DuBuque',		
			'Phyllis_Stamm@hotmail.com',		
			'Makenna_Schmitt89',		
			'e1mrWjW3LhQmBIP',		
			'1978-04-27',
            4	
		),
		(
			'Doreen Parisian',		
			'Tyrone.Reichert82@gmail.com',		
			'Lloyd57',		
			'8ajovAhcz8wB_RT',		
			'1994-11-26',
            1		
		),
		(
			'Casey Cormier IV',		
			'Maggie_Harber@hotmail.com',		
			'Jalen74',		
			'CkCJ46bJCmYUCGo',		
			'1997-08-29',
            2	
		),
		(
			'Billie Leffler',		
			'Rosemary_Hamill97@gmail.com',		
			'Oma.Watsica-Herman45',		
			'fKdpDhZ_RmyZnSg',		
			'2001-03-05',
            1	
		),
		(
			'Joy Hoeger III',		
			'Carl_Funk@gmail.com',		
			'Edythe35',		
			'5ArKjBnMItlir0j',		
			'2007-01-13',
            1		
		),
		(
			'Lloyd Cronin',		
			'Miranda_Champlin@hotmail.com',		
			'Alba.Orn33',		
			'JEyGmdQMLM0vMzg',		
			'1997-09-16',
            1	
		),
		(
			'Dr. Santiago Torphy',		
			'Theresa_Emmerich56@yahoo.com',		
			'Alice52',		
			'kKOKkiDBa4mVC1h',		
			'1996-01-07',
            1	
		),
		(
			'Geraldine Ratke',		
			'Michele_Hegmann@gmail.com',		
			'Octavia77',		
			'S5YNQYIpHL5n_5L',		
			'2000-04-20',
            1	
		),
		(
			'Dr. Lionel Goldner',		
			'Sandy_Cartwright@hotmail.com',		
			'Sylvester.Roberts',		
			'EQngxj1_SEjk9un',		
			'1977-03-23',
            1		
		),
		(
			'Dr. Ellis OKeefe',		
			'Dennis.Towne@gmail.com',		
			'Mariam33',		
			'ql5aFx8FwdDSkbG',		
			'1995-09-02',
            2	
		),
		(
			'Mr. Steve Bernier',		
			'Mario.Mayer50@hotmail.com',		
			'Angeline78',		
			'jAfHD12fXACzdG8',		
			'1977-09-05',
            1		
		),
		(
			'Lora Stanton',		
			'Heather_Crooks19@gmail.com',		
			'Carole_Doyle85',		
			'meMFDuP5nRMHUAq',		
			'1976-01-25',
            1		
		),
		(
			'Jenny Lang-Watsica',		
			'Irene.Rice@yahoo.com',		
			'Clement_Russel52',		
			'xcwC2JqmtTMD1sY',		
			'1992-08-16',
            1		
		),
		(
			'Mrs. Sophie Treutel-Tromp',		
			'Hubert_Treutel23@gmail.com',		
			'Karen.Corwin50',		
			'jFVHSs47wLWh_w8',		
			'1977-02-12',
            3	
		),
		(
			'Jenny OConnell',		
			'Rochelle.Mosciski31@hotmail.com',		
			'Ramiro.Kuphal',		
			'LW24rqjyZ68PzZb',		
			'1974-08-30',
            1		
		),
		(
			'Marian Murray',		
			'Dwight_Hyatt@hotmail.com',		
			'Sharon_DuBuque',		
			'PyDWCZPWvCMGl9j',		
			'1978-12-01',
            1		
		),
		(
			'Jesse Hartmann',		
			'Arthur.Weissnat@hotmail.com',		
			'Ronaldo.Nolan',		
			'3pfJIGHO0rBos98',		
			'1999-11-13',
            2		
		),
		(
			'Dave Murphy',		
			'Felipe_Swaniawski78@hotmail.com',		
			'Gerard.Hegmann1',		
			'Ko77_UY0WUNMn8h',		
			'1974-12-27',
            1		
		),
		(
			'Irene Greenholt DVM',		
			'Tracey_Leffler98@gmail.com',		
			'Johanna_Goldner-Boyer13',		
			'U5D8muz8ifNsVtD',		
			'1999-01-02',
            1		
		),
		(
			'Dr. Pedro Bruen',		
			'Lee_Dickinson68@hotmail.com',		
			'Ardella.Trantow',		
			'5vT73V7Gsb3OdPW',		
			'1975-10-03',
            2		
		),
		(
			'Carol Strosin',		
			'Shannon.Rice@gmail.com',		
			'Dane81',		
			'QZQFh0Hl2x0Jq0X',		
			'1977-01-22',
            1	
		),
		(
			'David Emard',		
			'Emanuel_Jerde18@gmail.com',		
			'Verona10',		
			'Uc6LL922mrkrRQi',		
			'1982-09-27',
            1		
		),
		(
			'Molly Parker MD',		
			'Douglas_Nader72@gmail.com',		
			'Minerva_Breitenberg',		
			'NNa0ePZEwi8w_qE',		
			'1997-04-09',
            1	
		),
		(
			'Mable Johnson',		
			'Caleb.Jacobs@yahoo.com',		
			'Adriana43',		
			'mMVmS8dBqhxv2UM',		
			'1977-09-30',
            1		
		)

INSERT INTO lyfter_car_rental.Cars(brand, model, fabrication_year, car_status)
    VALUES (1, 'Focus', 2001, 1),
    (6, 'Sentra', 2011, 5),
    (8, 'Wrangler', 2014, 4),
    (10, 'Lancer', 2008, 1),
    (4, 'RS GT3', 2016, 2),
    (2, 'Miata', 2021, 6),
    (7, 'Sorento', 2022, 7),
    (5, 'Yaris', 2021, 3),
    (5, 'Supra', 2016, 5),
    (10, 'Montero', 2019, 8)

INSERT INTO lyfter_car_rental.Rentals(user_ID, car_ID, rental_status)
	VALUES(32,5,1),
	(44,3,2),
	(14,4,1),
	(2,1,3),
	(36,6,5),
	(34,3,1),
	(41,8,2),
	(23,1,5),
	(22,10,6),
	(50,7,5),
	(12,3,2),
	(45,7,5),
	(21,8,4),
	(18,4,5),
	(43,7,3),
	(12,1,1),
	(42,3,2),
	(47,2,4),
	(29,6,6),
	(34,8,4)
