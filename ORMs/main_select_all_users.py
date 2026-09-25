from Connection_DB import MakeConectionDb
from select_all_users import SelectAllUsers

def main():

    database = MakeConectionDb()
        
    database.connect()
    
    all_users = SelectAllUsers(database.engine)

    all_users.Select_all_users()

if __name__ == "__main__":
    main()