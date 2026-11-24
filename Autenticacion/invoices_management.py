from sqlalchemy import insert, update, delete, select
from create_tables import invoices_table

class InvoicesManagement:

    def __init__(self, engine):
        self.engine = engine

    def create_new_invoice(self, user_id_input, fruit_id_input, quantity_input, price_input, invoices_date_input):
        try:
            query = (insert(invoices_table).values(user_id = user_id_input, fruit_id = fruit_id_input, quantity = quantity_input, price = price_input, invoices_date = invoices_date_input).returning(invoices_table.c.id))
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                invoices_id = result.scalar_one()

                return invoices_id

        except Exception as e:
            return f"Database_error: {e}"

    def modify_invoice(self, id_input, user_id_input, fruit_id_input, quantity_input, price_input, invoices_date_input):
        try:
            query = (update(invoices_table).where(invoices_table.c.id == id_input).values(user_id = user_id_input, fruit_id = fruit_id_input, quantity = quantity_input, price = price_input, invoices_date = invoices_date_input))
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "invoices_not_found"

                return "invoices_modified"

        except Exception as e:
            return f"Database_error: {e}"

    def dele_invoice(self, id_input):
        try:
            query = delete(invoices_table).where(invoices_table.c.id == id_input)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "invoices_not_found."

                return "invoices_deleted."

        except Exception as e:
            return f"Database_error: {e}"

    def select_invoices(self, id_input):
        try:
            query = select(invoices_table.c.user_id, invoices_table.c.fruit_id, invoices_table.c.quantity, invoices_table.c.price, invoices_table.c.invoices_date).where(invoices_table.c.id == id_input)
            with self.engine.connect() as conn:
                result = conn.execute(query).fetchall()

                if not result:
                    return "invoices_not_found"

                return result

        except Exception as e:
            print("Databse_error", e)

    def select_all_invoices(self):
        try:
            query = select(invoices_table)
            with self.engine.connect() as conn:

                result = conn.execute(query).fetchall()

                for row in result:

                    print(row)

        except Exception as e:
            return f"Database_error: {e}"