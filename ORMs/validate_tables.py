from sqlalchemy import inspect
from Create_db_tables import metadata_obj


class ValidateTablesExist:

    def __init__(self, engine):
        self.engine = engine

    def check_tables_exist(self):

        tables = ["Address","Automoviles","Users"]

        try:
            inspector = inspect(self.engine)

            for table in tables:

                if not inspector.has_table(
                    table,
                    schema="cars_inventory"
                ):
                    print(f"The Table {table} do not exist.")
                    print("Creating missing tables...")
                    metadata_obj.create_all(self.engine)
                    return "The tables are all good."
                
            return "The tables are all good."

        except Exception as e:
            return f"Error validating tables: {e}"