from script_backup.get_db_info import make_csv_archive
from database.Database_connection import Database
from datetime import date
import csv
import os

def create_csv(name, colums, data):

    os.makedirs("db_backups", exist_ok=True)

    file_name = f"{name}_backup_{date.today()}.csv"

    file_path = os.path.join("db_backups", file_name)


    with open(file_path, "w" ,encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(colums)

        for row in data:
            writer.writerow(row) 

database = Database()

archive = make_csv_archive(database)

users_columns, users = archive.get_db_users()
cars_columns, cars = archive.get_db_cars()
rentals_columns, rentals = archive.get_db_rentals()

create_csv("users",users_columns, users)
create_csv("cars",cars_columns, cars)
create_csv("rentals",rentals_columns, rentals)