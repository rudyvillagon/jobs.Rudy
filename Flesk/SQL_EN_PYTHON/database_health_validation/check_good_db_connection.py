

class CheckConnection:

    def __init__(self, database):
            self.connection = database.connection

    def check_good_connection(self):
        cursor = self.connection.cursor()

        try:
            cursor.execute(
                            "SELECT 1")
            result = cursor.fetchone()

            if result == (1,):
                return True
            else:
                return False

        finally:
            cursor.close()
