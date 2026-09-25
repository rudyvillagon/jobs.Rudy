from Create_db_tables import users_table
from sqlalchemy import select

class SelectAllUsers:

    def __init__(self, engine):
        self.engine = engine

    def Select_all_users(self):

        try:

            query = select(users_table)

            with self.engine.connect() as conn:
        
                result = conn.execute(query).fetchall()

                for row in result:

                    print(row)

        except Exception as e:
            print("Databse_error", e)