from Connection_DB import MakeConectionDb
from validate_tables import ValidateTablesExist


def main():

    database = MakeConectionDb()

    database.connect()

    validator = ValidateTablesExist(database.engine)

    result = validator.check_tables_exist()

    print(result)

if __name__ == "__main__":
    main()