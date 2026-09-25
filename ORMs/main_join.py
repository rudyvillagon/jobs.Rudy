from Connection_DB import MakeConectionDb
from join_user_with_car import JoinCarsWithUsers


def main():

    database = MakeConectionDb()
    
    database.connect()

    Join_query = JoinCarsWithUsers(database.engine)

    result = Join_query.join_both(1, 1)
    
    print(result)

if __name__ == "__main__":
    main()