class NewRental:

    def __init__(self, database):
        self.connection = database.connection

    def new_rent_car(self, data):

        user_ID = data.get("id_user")
        car_ID = data.get("id_car")
        new_rental_status = 2
        new_status_car = 3


        cursor = self.connection.cursor()

        try:
            cursor.execute(
                "SELECT user_status FROM lyfter_car_rental.Users WHERE id=%s",
                (user_ID,)
            )

            result1 = cursor.fetchone()

            if result1 is not None:
                result1 = result1[0]

            cursor.execute(
                "SELECT car_status FROM lyfter_car_rental.Cars WHERE id=%s",
                (car_ID,)
            )

            result2 = cursor.fetchone()

            if result2 is not None:
                result2 = result2[0]

            if result1 is None:
                return "user_not_exist"
            elif result1 != 1:
                return "user_not_active"
            elif result2 is None:
                return "The car_not_exist"
            elif result2 != 1:
                return "car_not_available"
            else:
                cursor.execute(
                    "INSERT INTO lyfter_car_rental.Rentals (user_id, car_id, rental_status) values(%s, %s, %s);",
                    (user_ID, car_ID, new_rental_status,)
                    )
                cursor.execute(
                    "UPDATE lyfter_car_rental.Cars SET car_status= %s WHERE id =%s",
                    (new_status_car, car_ID,)
                    )

                self.connection.commit()

        except Exception:
            self.connection.rollback()
            raise

        finally:
            cursor.close()
