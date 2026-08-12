from database.Database_connection import Database

class CheckCarsAvailable:

    def __init__(self, database):
            self.connection = database.connection

    def check_cars(self):
        cursor = self.connection.cursor()

        try:
            cursor.execute("""SELECT EXISTS (SELECT 1 FROM lyfter_car_rental.cars
                    WHERE car_status = 1)""")
            result = cursor.fetchone()

            if result == (True,):
                print("The table has at least one car available. ")
            else:
                print("there are no cars available.")
        finally:
            cursor.close()

db = Database()

check = CheckCarsAvailable(db)

check.check_cars()

db.close()