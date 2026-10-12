from Connection_DB import MakeConectionDb
from users_management import UsersManagement

def main():

    database = MakeConectionDb()
    
    database.connect()

    user_manage = UsersManagement(database.engine)

    user_name_input = "Marcs346"
    full_name_input = "Marco Rojas Arce"
    email_input = "MarcoR1999@gmail.com"

    result_1 = user_manage.create_user(user_name_input, full_name_input, email_input)

    print(f"The new user Id is {result_1}")

    user_id_input = result_1

    mod_user_name = "MarcRo11"

    result_2 = user_manage.modify_user(user_id_input, mod_user_name)

    deled_user_id = user_id_input

    print(result_2)

    result_3 =  user_manage.dele_user(deled_user_id)

    print(result_3)

if __name__ == "__main__":
    main()