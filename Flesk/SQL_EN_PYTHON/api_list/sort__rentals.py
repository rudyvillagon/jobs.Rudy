class SortRentals:

    def __init__(self, database):
            self.connection = database.connection

    def rentals_sort(self,filters):

        query = "SELECT * FROM lyfter_car_rental.Rentals"
        values = []

        if filters:
            conditions = []
            columns_set = {
                "id",
                "user_id",
                "car_id",
                "rent__date",
                "rental_status",
            }

            for column, value in filters.items():
                if column not in columns_set:
                    raise ValueError(f"column not allowed: {column} ")
                
                conditions.append(f"{column} = %s")
                values.append(value)

            query += " WHERE " + " AND ".join(conditions)

        cursor = self.connection.cursor()
        cursor.execute(query, values)
        return cursor.fetchall()