from Connection_DB import MakeConectionDb
from cars_management import CarManagement

def main():

    database = MakeConectionDb()
        
    database.connect()

    all_cars = CarManagement(database.engine)

    all_cars.select_all_cars()

    all_cars.select_all_car_not_associated()

if __name__ == "__main__":
    main()