from Flesk.SQL_EN_PYTHON.database.Database_connection import Database
from .check_good_db_connection import CheckConnection
from .check_files_db_connection import CheckFilesConnection
from .check_cars_table import CheckCarsAvailable

class ValidationHealthScript:

    def __init__(self, database):
                self.connection = database.connection

    def check_good_connections(self):
            check_conne = CheckConnection(self)
            if not check_conne.check_good_connecion():
                return "DB ERROR. No cars available1"
            check_file = CheckFilesConnection(self)
            if not check_file.check_files_exist():
                return "DB ERROR. No cars available2"
            check_car = CheckCarsAvailable(self)
            if not check_car.check_cars():
                return "DB ERROR. No cars available3"
            return "DB OK. Operating system is functioning normally"

if __name__ == "__main__":
    db = Database()

    VHS = ValidationHealthScript
    result = VHS.check_good_connections(db)
    print(result)

    db.close()