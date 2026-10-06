from Connection_DB import MakeConectionDb
from cars_management import CarManagement


def main():

    database = MakeConectionDb()
    
    database.connect()

    join_query = CarManagement(database.engine)

    input_car_id =  1

    input_user_id = 1

    result = join_query.join_both(input_car_id, input_user_id)
    
    print(result)

if __name__ == "__main__":
    main()