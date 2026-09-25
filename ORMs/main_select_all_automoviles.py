from Connection_DB import MakeConectionDb
from select_all_automoviles import SelectAllAutomoviles

def main():

    database = MakeConectionDb()
        
    database.connect()

    all_automoviles = SelectAllAutomoviles(database.engine)

    all_automoviles.Select_all_Automoviles()

if __name__ == "__main__":
    main()