

class CheckCarsAvailable:

    def __init__(self, database):
            self.connection = database.connection

    def check_cars(self):
        cursor = self.connection.cursor()

        try:
            cursor.execute("""SELECT EXISTS (SELECT 1 FROM lyfter_car_rental.Cars
                    WHERE car_status = 1)""")
            result = cursor.fetchone()

            if result == (True,):
                return True
            else:
                return False
        finally:
            cursor.close()

