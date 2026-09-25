from Create_db_tables import automoviles
from sqlalchemy import select

class SelectAllAutomoviles:

    def __init__(self, engine):
        self.engine = engine

    def Select_all_Automoviles(self):

        try:

            query = select(automoviles)

            with self.engine.connect() as conn:

                result = conn.execute(query).fetchall()

                for row in result:

                    print(row)

        except Exception as e:
            print("Databse_error", e)            