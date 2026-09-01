

class CheckFilesConnection:

    def __init__(self, database):
            self.connection = database.connection

    def check_files_exist(self):
        cursor= self.connection.cursor()

        try:
            tables = ["users","cars","rentals"]
            for table in tables:
                cursor.execute("""SELECT EXISTS (SELECT 1 FROM information_schema.tables
                WHERE table_schema = 'lyfter_car_rental'
                AND table_name = %s)
                """,(table,))
                result = cursor.fetchone()


                if result == (True,):
                    continue
                else:
                    return False
        finally:
            cursor.close()
        return True



