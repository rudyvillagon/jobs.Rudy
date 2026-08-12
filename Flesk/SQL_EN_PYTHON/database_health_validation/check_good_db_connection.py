from database.Database_connection import Database

class CheckConnection:

    def __init__(self, database):
            self.connection = database.connection

    def check_good_connecion(self):
        cursor = self.connection.cursor()

        try:
            cursor.execute(
                            "SELECT 1")
            result = cursor.fetchone()

            if result == (1,):
                print("DB is working correctly")
            else:
                print("DB ERROR, Theres no data")

        finally:
            cursor.close()

db = Database()
check = CheckConnection(db)
check.check_good_connecion()
db.close()