from Connection_DB import MakeConectionDb
from address_management import AddressManagement

def main():

    database = MakeConectionDb()
            
    database.connect()
        
    all_addresses = AddressManagement(database.engine)

    all_addresses.select_all_addresses()

    specific_word= "Calle"

    all_addresses.select_all_address_with_specific_word(specific_word)

if __name__ == "__main__":
    main()