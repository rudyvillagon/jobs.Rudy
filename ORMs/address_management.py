from sqlalchemy import insert, update, delete, select
from Create_db_tables import address

class AddressManagement:

    def __init__(self, engine):
        self.engine = engine

    def create_address(self, user_id_input, full_address_input):
        try:
            query = (insert(address).values(user_id = user_id_input, full_address = full_address_input).returning(address.c.id))
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                address_id = result.scalar_one()

                return address_id

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
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "Address_not_found."

                return "Address_deleted"
        
        except Exception as e:
            return f"Database_error: {e}"

    def select_all_addresses(self):

        try:

            query = select(address)

            with self.engine.connect() as conn:

                result = conn.execute(query).fetchall()

                for row in result:

                    print(row)

        except Exception as e:
            print("Databse_error", e) 