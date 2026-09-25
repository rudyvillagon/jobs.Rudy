class SortCars:

    def __init__(self, database):
            self.connection = database.connection

    def cars_sort(self,filters):

        query = "SELECT * FROM lyfter_car_rental.Cars"
        values = []

        if filters:
            conditions = []
            columns_set = {
                "id",
                "brand",
                "model",
                "fabrication_year",
                "car_status",
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