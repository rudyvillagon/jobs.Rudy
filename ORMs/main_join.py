from Connection_DB import MakeConectionDb
from cars_management import CarManagement


def main():

    database = MakeConectionDb()
    
    database.connect()

    Join_query = CarManagement(database.engine)

    result = Join_query.join_both(1, 1)
    
    print(result)

if __name__ == "__main__":
    main()