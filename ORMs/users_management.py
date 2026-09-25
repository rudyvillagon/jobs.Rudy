from sqlalchemy import insert, update, delete
from Create_db_tables import users_table

class UsersManagement:

    def __init__(self, engine):
        self.engine = engine

    def create_user(self ,User_name ,Full_name ,Email):
        try:
            query = insert(users_table).values(user_name= User_name, full_name= Full_name, email= Email)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                return "User_regist_created."

        except Exception as e:
            return f"Database_error: {e}"

    def modify_user(self ,User_id ,Mod_user_name):
        try:
            query = update(users_table).where(users_table.c.id == User_id).values(user_name= Mod_user_name)
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