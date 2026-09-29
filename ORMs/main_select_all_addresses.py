from Connection_DB import MakeConectionDb
from address_management import AddressManagement

def main():

    database = MakeConectionDb()
            
    database.connect()
        
    all_addresses = AddressManagement(database.engine)

    all_addresses.Select_all_Addresses()

if __name__ == "__main__":
    main()