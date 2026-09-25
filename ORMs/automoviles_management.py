from sqlalchemy import insert, update, delete
from Create_db_tables import automoviles

class AutomovileManagement:

    def __init__(self, engine):
        self.engine = engine

    def create_automovile(self, Brand, Model, Year, License_plate):
        try:
            query = insert(automoviles).values( brand = Brand, model = Model, year = Year, license_plate = License_plate)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                return "Automovile_regist_created."

        except Exception as e:
            return f"Database_error: {e}"

    def modifi_automovile(self, automovile_id, modified_year):
        try:
            query = update(automoviles).where(automoviles.c.id == automovile_id).values(year = modified_year)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "Automovile_not_found."

                return "Automovile_modified."
            
        except Exception as e:
            return f"Database_error: {e}"
    
    def dele_automovile(self, deled_id):
        try:
            query = delete(automoviles).where(automoviles.c.id == deled_id)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "Automovile_not_found."

                return "Automovile_deleted."

        except Exception as e:
            return f"Database_error: {e}"