from sqlalchemy import insert, update, delete
from Create_db_tables import address

class AddressManagement:

    def __init__(self, engine):
        self.engine = engine

    def create_address(self, user_id, Full_address):
        try:
            query = insert(address).values(User_id = user_id, full_address = Full_address)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                return "Address_created"

        except Exception as e:
            return f"Database_error: {e}"

    def modifi_address(self, address_id, modified_address):
        try: 
            query = update(address).where(address.c.id == address_id).values(full_address = modified_address)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "Address_not_found."

                return "Address_modified"
        
        except Exception as e:
            return f"Database_error: {e}"

    def dele_address(self, address_id):
        try:
            query = delete(address).where(address.c.id == address_id)
            with self.engine.connec() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "Address_not_found."

                return "Address_deleted"
        
        except Exception as e:
            return f"Database_error: {e}"