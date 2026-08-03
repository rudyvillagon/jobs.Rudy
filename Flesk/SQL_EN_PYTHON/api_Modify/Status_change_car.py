
class ChangeStatusCar:

    def __init__(self, database):
        self.connection = database.connection

    def change_car_status(self, data):

        id = data.get("id")
        New_status = data.get("car_status")

        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT car_status FROM lyfter_car_rental.Cars WHERE id =%s",
            (id,)
        )

        result = cursor.fetchone()

        if result is None:
            print("the car don't exist.")
        elif result[0] == New_status:
            print("The car already has that status.")
        else:
            cursor.execute(
                "UPDATE lyfter_car_rental.Cars SET car_status= %s WHERE id =%s",
            (New_status, id)
            )
            print("Successfully updated Car")

        self.connection.commit()
        print("commited.")

        cursor.close()

