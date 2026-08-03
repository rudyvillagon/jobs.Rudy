class ChangeCarStatusDisable:

    def __init__(self, database):
        self.connection = database.connection

    def disable_car(self, data):

        car_id= data.get("id")
        disable_car_status = 8

        cursor = self.connection.cursor()

        try:
            cursor.execute(
                "SELECT car_status FROM lyfter_car_rental.cars WHERE id=%s",
                (car_id,)
            )

            result = cursor.fetchone()

            if result is None:
                print("The car doesn't exist. ")
            elif result[0] == disable_car_status:
                print("The car has already been retired. ")
            else:
                cursor.execute(
                    "UPDATE lyfter_car_rental.cars SET car_status= %s WHERE id= %s",
                    (disable_car_status, car_id)
                )
                print("The car has been retired.")

                self.connection.commit()
                print("commited.")
        finally:
            cursor.close()
            print("Cursor closed.")

