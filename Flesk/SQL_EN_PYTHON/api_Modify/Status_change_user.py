
class ChangeStatusUser:

    def __init__(self, database):
        self.connection = database.connection

    def change_user_status(self, data):

        user_name = data.get("user_name")
        New_status = data.get("user_status")

        cursor = self.connection.cursor()

        try:
            cursor.execute(
                "SELECT user_status FROM lyfter_car_rental.Users WHERE user_name =%s",
                (user_name,)
            )

            result = cursor.fetchone()

            if result is None:
                return "user_not_exist"
            elif result[0] == New_status:
                return "user_already_has_that_status"
            else:
                cursor.execute(
                    "UPDATE lyfter_car_rental.Users SET user_status= %s WHERE user_name =%s",
                    (New_status, user_name)
                    )
                print("Successfully updated User")

                self.connection.commit()
                print("commited.")

        finally:
            cursor.close()

