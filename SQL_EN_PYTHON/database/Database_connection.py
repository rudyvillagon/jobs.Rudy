import psycopg2

class Database:

    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            port=5432,
            user="postgres",
            password="123456",
            dbname="car_rental"
        )



    def close(self):
        self.connection.close()