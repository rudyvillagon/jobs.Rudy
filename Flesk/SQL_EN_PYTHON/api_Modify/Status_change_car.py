
class ChangeStatusCar:

    def __init__(self, database):
        self.connection = database.connection

    def change_car_status(self, data):

        id = data.get("id")
        New_status = data.get("car_status")

        cursor = self.connection.cursor()

        try:
            cursor.execute(
                "SELECT car_status FROM lyfter_car_rental.Cars WHERE id =%s",
                (id,)
            )

            result = cursor.fetchone()

            if result is None:
                return "car_not_found"
            elif result[0] == New_status:
                return "car_already_has_that_status"
            else:
                cursor.execute(
                    "UPDATE lyfter_car_rental.Cars SET car_status= %s WHERE id =%s",
                (New_status, id)
                )


            self.connection.commit()
            print("commited.")

        finally:
            cursor.close()

