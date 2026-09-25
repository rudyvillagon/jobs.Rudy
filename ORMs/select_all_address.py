from Create_db_tables import address
from sqlalchemy import select

class SelectAllAddresses:

    def __init__(self, engine):
        self.engine = engine

    def Select_all_Addresses(self):

        try:

            query = select(address)

            with self.engine.connect() as conn:

                result = conn.execute(query).fetchall()

                for row in result:

                    print(row)

        except Exception as e:
            print("Databse_error", e)            