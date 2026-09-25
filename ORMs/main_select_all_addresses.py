from Connection_DB import MakeConectionDb
from select_all_address import SelectAllAddresses

def main():

    database = MakeConectionDb()
            
    database.connect()
        
    all_addresses = SelectAllAddresses(database.engine)

    all_addresses.Select_all_Addresses()

if __name__ == "__main__":
    main()