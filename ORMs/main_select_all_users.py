from Connection_DB import MakeConectionDb
from users_management import UsersManagement

def main():

    database = MakeConectionDb()
        
    database.connect()
    
    all_users = UsersManagement(database.engine)

    all_users.select_all_users()

    all_users.select_all_users_with_more_cars_then_one()

if __name__ == "__main__":
    main()