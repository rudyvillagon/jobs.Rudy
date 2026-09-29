from Connection_DB import MakeConectionDb
from users_management import UsersManagement

def main():

    database = MakeConectionDb()
        
    database.connect()
    
    all_users = UsersManagement(database.engine)

    all_users.Select_all_users()

if __name__ == "__main__":
    main()