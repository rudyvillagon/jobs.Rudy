from Flesk.SQL_EN_PYTHON.database.Database_connection import Database
from .check_good_db_connection import CheckConnection
from .check_files_db_connection import CheckFilesConnection
from .check_cars_table import CheckCarsAvailable

class ValidationHealthScript:

    def __init__(self, database):
                self.connection = database.connection

    def check_good_connections(self):
            check_conne = CheckConnection(self)
            if not check_conne.check_good_connection():
                return "DB ERROR. No connection available"
            check_file = CheckFilesConnection(self)
            if not check_file.check_files_exist():
                return "DB ERROR. Required tables are not available"
            check_car = CheckCarsAvailable(self)
            if not check_car.check_cars():
                return "DB ERROR. No cars available"
            return "DB OK. Operating system is functioning normally"

if __name__ == "__main__":
    db = Database()

    VHS = ValidationHealthScript(db)
    result = VHS.check_good_connections()
    print(result)

    db.close()