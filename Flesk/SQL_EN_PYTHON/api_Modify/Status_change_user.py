
class ChangeStatusUser:

    def __init__(self, database):
        self.connection = database.connection

    def change_user_status(self, data):

        user_name = data.get("user_name")
        New_status = data.get("user_status")

        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT user_status FROM lyfter_car_rental.Users WHERE user_name =%s",
            (user_name,)
        )

        result = cursor.fetchone()

        if result is None:
            print("the user don't exist. ")
        elif result[0] == New_status:
            print("The user already has that status. ")
        else:
            cursor.execute(
                "UPDATE lyfter_car_rental.Users SET user_status= %s WHERE user_name =%s",
                (New_status, user_name)
                )
            print("Successfully updated User")

            self.connection.commit()
            print("commited.")
            cursor.close()

