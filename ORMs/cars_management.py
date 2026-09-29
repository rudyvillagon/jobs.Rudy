from sqlalchemy import insert, update, delete, select
from Create_db_tables import cars

class CarManagement:

    def __init__(self, engine):
        self.engine = engine

    def create_car(self, User_id, Brand, Model, Year, License_plate):
        try:
            query = insert(cars).values(user_id = User_id, brand = Brand, model = Model, year = Year, license_plate = License_plate)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                return "Car_regist_created."

        except Exception as e:
            return f"Database_error: {e}"

    def modifi_car(self, car_id, modified_year):
        try:
            query = update(cars).where(cars.c.id == car_id).values(year = modified_year)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "Car_not_found."

                return "Car_modified."
            
        except Exception as e:
            return f"Database_error: {e}"
    
    def dele_car(self, deled_id):
        try:
            query = delete(cars).where(cars.c.id == deled_id)
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                if result.rowcount == 0:
                    return "Car_not_found."

                return "Car_deleted."

        except Exception as e:
            return f"Database_error: {e}"


    
    def Select_all_cars(self):
    
        try:
    
            query = select(cars)
    
            with self.engine.connect() as conn:
    
                result = conn.execute(query).fetchall()
    
                for row in result:
    
                    print(row)
    
        except Exception as e:
            print("Databse_error", e)  

    def join_both(self,car_id, user_id):

        try:

        
            query = select(cars.c.User_id).where(
                cars.c.id == car_id
            )
            with self.engine.connect() as conn:

                result = conn.execute(query).fetchone()
        
                if result is None:
                    return "Car_dont_exist"

                automovile_user = result[0]


                if automovile_user is not None:
                    return "Car_already_link_with_a_user"
        
                update_user_car = update(cars).where(cars.c.id == car_id).values(User_id = user_id)
        
                conn.execute(update_user_car)
                conn.commit()

                return "User_linked_correctly"

        except Exception as e:
                    print("Databse_error", e)