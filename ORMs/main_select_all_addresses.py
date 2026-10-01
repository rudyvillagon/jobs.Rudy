from Connection_DB import MakeConectionDb
from address_management import AddressManagement

def main():

    database = MakeConectionDb()
            
    database.connect()
        
    all_addresses = AddressManagement(database.engine)

    all_addresses.select_all_addresses()

if __name__ == "__main__":
    main()