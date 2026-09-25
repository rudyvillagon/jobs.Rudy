
class ChangeDefaulterUser:

    def __init__(self, database):
        self.connection = database.connection

    def change_user_defaulter(self, data):

        user_id = data.get("user_id")
        defaulter_status = 5
        overdue_status = 4

        cursor = self.connection.cursor()

        try:
            cursor.execute(
                "SELECT 1 FROM lyfter_car_rental.Rentals WHERE user_id =%s AND rental_status = %s",
                (user_id,overdue_status,)
            )

            result = cursor.fetchone()

            if result is None:
                return "user_has_no_rentals"
            else:
                cursor.execute(
                    "UPDATE lyfter_car_rental.Users SET user_status= %s WHERE id =%s",
                    (defaulter_status, user_id)
                    )
                print("The user has been flagged as defaulter.")

                self.connection.commit()
                print("commited.")
        finally:
            cursor.close()
