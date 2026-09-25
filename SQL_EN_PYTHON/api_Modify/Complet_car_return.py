class CarReturn:

    def __init__(self, database):
        self.connection = database.connection

    def car_return(self, data):

        rental_id = data.get("id")
        new_rental_status = 4
        new_car_status = 2

        cursor = self.connection.cursor()

        try:
            cursor.execute(
                "SELECT rental_status FROM lyfter_car_rental.rentals WHERE id=%s",
                (rental_id,)
            )

            result = cursor.fetchone()

            cursor.execute(
                "SELECT car_id FROM lyfter_car_rental.rentals WHERE id=%s",
                (rental_id,)
            )

            car_id = cursor.fetchone()

            if car_id is not None:
                car_id= car_id[0]

            if result is None:
                return "invoice_not_exist"
            elif result[0] == new_rental_status:
                return "vehicle_already_returned"
            else:
                cursor.execute(
                    "UPDATE lyfter_car_rental.Rentals SET rental_status= %s WHERE id= %s",
                    (new_rental_status, rental_id)
                )
                cursor.execute(
                    "UPDATE lyfter_car_rental.cars SET car_status= %s WHERE id= %s",
                    (new_car_status, car_id)
                )

                self.connection.commit()


        finally:
            cursor.close()
            print("Connection Close")
