from sqlalchemy.orm import Session 
from relations import User
from Connection_DB import MakeConectionDb

class InformationConsultation:

    def __init__(self):
        db = MakeConectionDb()
        self.engine = db.engine

    def get_user_general_info(self, user_id):
        with Session(self.engine) as session:

            user = session.get(User,user_id)

            if user is not None:
                print("User:", user.full_name)

                for car in user.cars:
                    print("Car Id:", car.id, "Brand:", car.brand, "Model:", car.model, "Year:", car.year, "License Plate:", car.license_plate)

                for address in user.addresses:
                    print("Address id:", address.id, "Full address:", address.full_address)

            else:
                print ("User not found.")