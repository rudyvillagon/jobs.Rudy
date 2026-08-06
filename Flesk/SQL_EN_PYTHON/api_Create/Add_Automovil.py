class NewVehicle:

    def __init__(self, database):
        self.connection = database.connection

    def add_automovil(self, data):

        brand = data.get("brand")
        model = data.get("model")
        fabrication_year = data.get("fabrication_year")
        car_status = data.get("car_status")

        cursor = self.connection.cursor()

        try:
            cursor.execute(
                "INSERT INTO lyfter_car_rental.Cars (brand, model, fabrication_year, car_status) values (%s, %s, %s, %s);", (brand, model, fabrication_year, car_status)
            )

            self.connection.commit()

        except Exception:
            self.connection.rollback()
            raise

        finally:
            cursor.close()
