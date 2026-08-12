from database.Database_connection import Database

class CheckFilesConnection:

    def __init__(self, database):
            self.connection = database.connection

    def check_files_exist(self):
        cursor= self.connection.cursor()

        tables = ["Users","Cars","Rentals"]
        for table in tables:
            cursor.execute("""SELECT EXISTS (SELECT 1 FROM information_schema.tables
            WHERE table_schema = 'lyfter_car_rental'
            AND table_name = %s)
            """,(table,))
            result = cursor.fetchone()


            if result == (True,):
                print(f"The {table} table works correctly.")
            else:
                print(f"The {table} table works correctly.")



        cursor.close()

db = Database()
check = CheckFilesConnection(db)
check.check_files_exist()
db.close()



