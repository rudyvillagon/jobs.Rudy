from Flesk.SQL_EN_PYTHON.database.Database_connection import Database
from .Inyect_with_faker import FakerInyect

class RunFakeInyection:

    def __init__(self, database):
                self.database = database
                self.connection= database.connection

    def run_faker(self):
            fake_intection_files = FakerInyect(self.database)

            try:
                fake_intection_files.inyect_users()
                fake_intection_files.inyect_cars()
                fake_intection_files.inyect_rentals()

            except Exception:
                    self.connection.rollback()
                    raise

            return "Faker Complete, you have inyected data."

if __name__ == "__main__":
    db = Database()

    RFI = RunFakeInyection(db)

    print(RFI.run_faker())

    db.close()
            