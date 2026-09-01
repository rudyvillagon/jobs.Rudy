class MakeCsvArchive:

    def __init__(self, database):
        self.connection = database.connection

    def get_db_users(self):

        query = "SELECT * FROM lyfter_car_rental.users"


        cursor = self.connection.cursor()
        cursor.execute(query)

        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        
        return columns, data

    def get_db_cars(self):
    
        query = "SELECT * FROM lyfter_car_rental.Cars"


        cursor = self.connection.cursor()
        cursor.execute(query)

        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()

        return columns, data

    def get_db_rentals(self):
    
        query = "SELECT * FROM lyfter_car_rental.Rentals"
    
    
        cursor = self.connection.cursor()
        cursor.execute(query)

        columns = [column[0] for column in cursor.description]
        data = cursor.fetchall()
        
        return columns, data

