from Connection_DB import MakeConectionDb
from cars_management import CarManagement

def main():

    database = MakeConectionDb()
    
    database.connect()

    car_manage = CarManagement(database.engine)

    user_id_input = 1
    brand_input = "Toyota"
    model_input = "Yaris"
    year_input = 2011
    license_plate_input = "fgd543"

    result_1 = car_manage.create_car(user_id_input, brand_input, model_input, year_input, license_plate_input)

    car_id = 1
    modified_year = 2010

    result_2 = car_manage.modifi_car(car_id, modified_year)

    deled_id = 1

    result_3 = car_manage.dele_car(deled_id)

    print(result_1)

    print(result_2)

    print(result_3)

if __name__ == "__main__":
    main()