from Connection_DB import MakeConectionDb
from users_management import UsersManagement

def main():

    database = MakeConectionDb()
    
    database.connect()

    user_manage = UsersManagement(database.engine)

    User_name = "Marcs346"
    Full_name = "Marco Rojas Arce"
    Email = "MarcoR1999@gmail.com"

    result_1 = user_manage.create_user(User_name, Full_name, Email)

    User_id = 1
    Mod_user_name = "MarcRo11"

    result_2 = user_manage.modify_user(User_id, Mod_user_name)

    deled_user_id = 1

    result_3 =  user_manage.dele_user(deled_user_id)

    print(result_1)

    print(result_2)

    print(result_3)

if __name__ == "__main__":
    main()