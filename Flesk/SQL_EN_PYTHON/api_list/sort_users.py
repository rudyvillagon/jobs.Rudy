class SortUsers:

    def __init__(self, database):
            self.connection = database.connection

    def users_sort(self,filters):

        query = "SELECT id, user_fullname, email, user_name, date_birth, user_status FROM lyfter_car_rental.Users"
        values = []

        if filters:
            conditions = []
            columns_set = {
                "id",
                "user_fullname",
                "email",
                "user_name",
                "date_birth",
                "user_status",
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
