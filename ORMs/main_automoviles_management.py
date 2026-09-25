from Connection_DB import MakeConectionDb
from automoviles_management import AutomovileManagement

def main():

    database = MakeConectionDb()
    
    database.connect()

    automovile_manage = AutomovileManagement(database.engine)

    Brand = "Toyota"
    Model = "Yaris"
    Year = 2011
    License_plate = "fgd543"

    result_1 = automovile_manage.create_automovile(Brand, Model, Year, License_plate)

    automovile_id = 1
    modified_year = 2010

    result_2 = automovile_manage.modifi_automovile(automovile_id, modified_year)

    deled_id = 1

    result_3 = automovile_manage.dele_automovile(deled_id)

    print(result_1)

    print(result_2)

    print(result_3)

if __name__ == "__main__":
    main()