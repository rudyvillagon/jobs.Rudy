from Connection_DB import MakeConectionDb
from cars_management import CarManagement


def main():

    database = MakeConectionDb()
    
    database.connect()

    join_query = CarManagement(database.engine)

    car_id =  join_query.get_car_id_by_license_plate("fgd543")

    user_id = join_query.get_user_id_by_email("MarcoR1999@gmail.com")

    result = join_query.join_both(car_id, user_id)
    
    print(result)

if __name__ == "__main__":
    main()