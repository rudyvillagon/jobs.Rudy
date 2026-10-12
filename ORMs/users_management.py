from sqlalchemy import insert, update, delete, select
from Create_db_tables import users_table

class UsersManagement:

    def __init__(self, engine):
        self.engine = engine

    def create_user(self ,user_name_input ,full_name_input ,email_input):
        try:
            query = (insert(users_table).values(user_name= user_name_input, full_name= full_name_input, email= email_input).returning(users_table.c.id))
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                user_id = result.scalar_one()

                return user_id

        except Exception as e:
            return f"Database_error: {e}"

    def modify_user(self ,user_id_input ,mod_user_name):
        try:
            query = update(users_table).where(users_table.c.id == user_id_input).values(user_name= mod_user_name)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "User_not_found."

                return "User_modified."

        except Exception as e:
            return f"Database_error: {e}"

    def dele_user(self, deled_user_id):
        try:
            query = delete(users_table).where(users_table.c.id == deled_user_id)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "User_not_found."

                return "User_deleted."

        except Exception as e:
            return f"Database_error: {e}"

    def select_all_users(self):

        try:

            query = select(users_table)

            with self.engine.connect() as conn:
        
                result = conn.execute(query).fetchall()

                for row in result:

                    print(row)

        except Exception as e:
            print("Databse_error", e)

    