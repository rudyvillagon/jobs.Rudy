from Connection_DB import MakeConectionDb
from ORMs.cars_management import CarManagement

def main():

    database = MakeConectionDb()
    
    database.connect()

    car_manage = CarManagement(database.engine)

    User_id = 1
    Brand = "Toyota"
    Model = "Yaris"
    Year = 2011
    License_plate = "fgd543"

    result_1 = car_manage.create_car(User_id, Brand, Model, Year, License_plate)

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