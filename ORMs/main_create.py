from Connection_DB import MakeConectionDb
from Create_db_tables import metadata_obj

def main():

    database = MakeConectionDb()

    database.connect()

    metadata_obj.create_all(database.engine)

if __name__ == "__main__":
    main()