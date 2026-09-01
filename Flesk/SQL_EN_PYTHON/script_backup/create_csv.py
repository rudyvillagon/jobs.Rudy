
from datetime import date
import csv
import os
class CreateCsvFiles:

    def create_csv(self, name, colums, data):

        os.makedirs("db_backups", exist_ok=True)

        file_name = f"{name}_backup_{date.today()}.csv"

        file_path = os.path.join("db_backups", file_name)


        with open(file_path, "w" ,encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(colums)

            for row in data:
                writer.writerow(row) 

