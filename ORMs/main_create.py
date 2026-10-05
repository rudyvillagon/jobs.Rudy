from Connection_DB import MakeConectionDb
from Create_db_tables import metadata_obj
from sqlalchemy import text


def main():

    database = MakeConectionDb()

    database.connect()

    try:
        with database.engine.begin() as conn:
            conn.execute(
                text("CREATE SCHEMA IF NOT EXISTS cars_inventory")
            )

        metadata_obj.create_all(database.engine)

        print("Schema and tables created Successfully.")

    except Exception as e:
        print(f"Database_error: {e}")

if __name__ == "__main__":
    main()