from sqlalchemy import inspect
from Create_db_tables import metadata_obj


class ValidateTablesExist:

    def __init__(self, engine):
        self.engine = engine

    def check_tables_exist(self):

        tables = ["Address","Cars","Users"]

        try:
            inspector = inspect(self.engine)

            missing_tables = []

            for table in tables:

                if not inspector.has_table(
                    table,
                    schema="cars_inventory"
                ):
                    missing_tables.append(table)

            if missing_tables:

                print(f"Missing tables: {missing_tables}")
                print("Creating missing tables...")

                metadata_obj.create_all(self.engine)

                return "Missing tables created successfully."
                
            return "The tables are all good."

        except Exception as e:
            return f"Error validating tables: {e}"