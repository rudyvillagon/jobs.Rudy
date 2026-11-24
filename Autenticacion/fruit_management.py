from sqlalchemy import insert, update, delete, select
from create_tables import fruit_table


class FruitManagement:
    def __init__(self, db):
        self.engine = db.engine

    
    def create_new_fruit(self, fruit_name_input, price_input, delivery_date_input, stock_input):
        try:
            query = (insert(fruit_table).values(fruit_name=fruit_name_input, price=price_input, delivery_date=delivery_date_input, stock=stock_input).returning(fruit_table.c.id))
            with self.engine.begin() as conn:
                result = conn.execute(query)

                invoices_id = result.scalar_one()

                return f"fruit added: {invoices_id}"

        except Exception as e:
            return f"Database_error: {e}"

    def modify_fruit(self, id_input, fruit_name_input, price_input, delivery_date_input, stock_input):
        try:
            query = update(fruit_table).where(fruit_table.c.id == id_input).values(fruit_name=fruit_name_input, price=price_input, delivery_date=delivery_date_input, stock=stock_input)
            with self.engine.begin() as conn:
                result = conn.execute(query)

                if result.rowcount == 0:
                    return "fruit_not_found"

                return "fruit_modified"

        except Exception as e:
            return f"Database_error: {e}"

    def dele_fruit(self, id_input):
        try:
            query = delete(fruit_table).where(fruit_table.c.id == id_input)
            with self.engine.begin() as conn:
                result = conn.execute(query)

                if result.rowcount == 0:
                    return "fruit_not_found."

                return "fruit_deleted."

        except Exception as e:
            return f"Database_error: {e}"

    def select_fruit(self, id_input):
        try:
            query = select(
                fruit_table.c.fruit_name,
                fruit_table.c.price,
                fruit_table.c.stock,
                fruit_table.c.delivery_date
            ).where(fruit_table.c.id == id_input)

            with self.engine.connect() as conn:
                result = conn.execute(query).fetchone()

                if not result:
                    return "fruit_not_found"

                return result

        except Exception as e:
            return f"Database_error: {e}"


    def select_all_fruit(self):
        try:
            query = select(fruit_table)
            with self.engine.connect() as conn:

                result = conn.execute(query).fetchall()

                return [dict(row._mapping) for row in result]

        except Exception as e:
            return f"Database_error: {e}"

