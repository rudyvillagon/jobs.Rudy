from Flesk.SQL_EN_PYTHON.database.Database_connection import Database
from faker import Faker
from faker_vehicle import VehicleProvider

class FakerInyect:

    def __init__(self, database):
            self.connection = database.connection

    def inyect_users(self):
            cursor = self.connection.cursor()
            fake = Faker()
            try:
                for _ in range(200):
                        user_fullname = fake.name()
                        email = fake.email()
                        user_name = fake.user_name()
                        password = fake.password()
                        date_birth = fake.date_of_birth()
                        user_status = fake.random_int(min=1, max=5)

                        cursor.execute(
                            "INSERT INTO lyfter_car_rental.Users (user_fullname, email, user_name, password, date_birth, user_status) values (%s, %s, %s, %s, %s, %s)ON CONFLICT DO NOTHING;", (user_fullname, email, user_name, password, date_birth, user_status)
                        )
                self.connection.commit()

            except Exception:
                self.connection.rollback()
                raise

            finally:
                cursor.close()

    def inyect_cars(self):
                cursor = self.connection.cursor()
                fake = Faker()
                fake.add_provider(VehicleProvider)
                try:
                    car_inyector = 0

                    while car_inyector < 100:
                            
                            vehicle = fake.vehicle_object()

                            brand_name = vehicle["Make"]
                            model = vehicle["Model"]
                            fabrication_year = vehicle["Year"]

                            cursor.execute(
                                """
                                SELECT id
                                FROM lyfter_car_rental.Brands_cars
                                WHERE brand_name = %s
                                """,
                                (brand_name,)
                            )

                            result = cursor.fetchone()

                            if result is None:
                                continue

                            brand = result[0]

                            car_status = fake.random_int(min=1, max=8)
    
                            cursor.execute(
                                "INSERT INTO lyfter_car_rental.Cars (brand, model, fabrication_year, car_status) values (%s, %s, %s, %s)ON CONFLICT DO NOTHING;", (brand, model, fabrication_year, car_status)
                            )

                            car_inyector+= 1
                            
                    self.connection.commit()
    
                except Exception:
                    self.connection.rollback()
                    raise

                finally:
                    cursor.close()

    def inyect_rentals(self):
                cursor = self.connection.cursor()
                fake = Faker()
                try:
                    for _ in range(100):
                            user_id = fake.random_int(min=1, max=200)
                            car_id = fake.random_int(min=1, max=100)
                            rent_date = fake.date_time()
                            rental_status = fake.random_int(min=1, max=6)
    
                            cursor.execute(
                                "INSERT INTO lyfter_car_rental.Rentals (user_id, car_id, rent_date, rental_status) values (%s, %s, %s, %s)ON CONFLICT DO NOTHING;", (user_id, car_id, rent_date, rental_status)
                            )
                    self.connection.commit()
    
                except Exception:
                    self.connection.rollback()
                    raise

                finally:
                    cursor.close()




