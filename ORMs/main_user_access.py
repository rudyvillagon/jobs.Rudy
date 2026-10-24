from bidirectional_user_access import InformationConsultation

def main():

    get_user_info = InformationConsultation()

    user_id = 2

    get_user_info.get_user_general_info(user_id)

if __name__ == "__main__":
    main()