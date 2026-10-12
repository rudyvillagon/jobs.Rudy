from sqlalchemy import insert, update, delete, select
from Create_db_tables import cars

class CarManagement:

    def __init__(self, engine):
        self.engine = engine

    def create_car(self, user_id_input, brand_input, model_input, year_input, license_plate_input):
        try:
            query = (insert(cars).values(user_id = user_id_input, brand = brand_input, model = model_input, year = year_input, license_plate = license_plate_input).returning(cars.c.id))
            with self.engine.connect() as conn:
                result = conn.execute(query)
                conn.commit()

                car_id = result.scalar_one()

                return car_id

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


    
    def select_all_cars(self):
    
        try:
    
            query = select(cars)
    
            with self.engine.connect() as conn:
    
                result = conn.execute(query).fetchall()
    
                for row in result:
    
                    print(row)
    
        except Exception as e:
            print("Databse_error", e)  

    def join_both(self,input_car_id, input_user_id):

        try:

        
            query = select(cars.c.user_id).where(
                cars.c.id == input_car_id
            )
            with self.engine.connect() as conn:

                result = conn.execute(query).fetchone()
        
                if result is None:
                    return "Car_dont_exist"

                automovile_user = result[0]


                if automovile_user is not None:
                    return "Car_already_link_with_a_user"
        
                update_user_car = update(cars).where(cars.c.id == input_car_id).values(user_id = input_user_id)
        
                conn.execute(update_user_car)
                conn.commit()

                return "User_linked_correctly"

        except Exception as e:
                    print("Databse_error", e)