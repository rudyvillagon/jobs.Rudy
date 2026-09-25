from Create_db_tables import automoviles
from sqlalchemy import select, update

class JoinCarsWithUsers:

    def __init__(self, engine):
        self.engine = engine

    def join_both(self,automovile_id, user_id):

        try:

        
            query = select(automoviles.c.User_id).where(
                automoviles.c.id == automovile_id
            )
            with self.engine.connect() as conn:

                result = conn.execute(query).fetchone()
        
                if result is None:
                    return "Automovile_dont_exist"

                automovile_user = result[0]


                if automovile_user is not None:
                    return "Automovile_already_link_with_a_user"
        
                update_user_car = update(automoviles).where(automoviles.c.id == automovile_id).values(User_id = user_id)
        
                conn.execute(update_user_car)
                conn.commit()

                return "User_linked_correctly"

        except Exception as e:
                    print("Databse_error", e)