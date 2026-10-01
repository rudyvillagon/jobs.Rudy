from Connection_DB import MakeConectionDb
from address_management import AddressManagement


def main():

    database = MakeConectionDb()

    database.connect()

    address_manage = AddressManagement(database.engine)

    full_address = "Avenida 8, Calle 21, Casa #145, Barrio Los Robles, San José, Costa Rica."

    result_1 = address_manage.create_address(1, full_address)

    modified_address = "Avenida 8, Calle 21, Casa #150, Barrio Los Robles, San José, Costa Rica."

    result_2 = address_manage.modifi_address(1, modified_address)

    result_3 = address_manage.dele_address(1)

    print(result_1)

    print(result_2)

    print(result_3)

if __name__ == "__main__":
    main()