from Flesk.SQL_EN_PYTHON.database.Database_connection import Database
from .create_csv import CreateCsvFiles
from .get_db_info import MakeCsvArchive

class RunCsvBackup:

    def __init__(self, database):
                self.database = database
                self.connection = database.connection

    def run_csv_creator(self):

            try:
                CCF = CreateCsvFiles()
                archive = MakeCsvArchive(self.database)

                users_columns, users = archive.get_db_users()
                cars_columns, cars = archive.get_db_cars()
                rentals_columns, rentals = archive.get_db_rentals()

                CCF.create_csv("users",users_columns, users)
                CCF.create_csv("cars",cars_columns, cars)
                CCF.create_csv("rentals",rentals_columns, rentals)

            except Exception:
                    self.connection.rollback()
                    raise
            
            return "CSV Complete, you have backup your data."

if __name__ == "__main__":
    db = Database()

    RCB = RunCsvBackup(db)

    print(RCB.run_csv_creator())

    db.close()