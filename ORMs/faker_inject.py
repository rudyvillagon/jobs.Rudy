
from relations import User, Car, Address
from Connection_DB import MakeConectionDb
from sqlalchemy.orm import Session 
from sqlalchemy import select
from faker import Faker
from faker_vehicle import VehicleProvider
import random

class FakerModels:

    def __init__(self):
        db = MakeConectionDb()
        self.engine = db.engine

    def fake_user_inject(self):
        fake = Faker()

        with Session(self.engine) as session:

            user = User(
                user_name = fake.user_name(),
                full_name = fake.name(),
                email = fake.email(),
            )

            session.add(user)
            session.commit()

            return user.id

    def fake_random_user_id_with_none(self, session):
        user_ids = session.scalars(
            select(User.id)
        ).all()

        if not user_ids:
            return None
        if random.random() < 0.3:
            return None

        return random.choice(user_ids)

    def fake_random_user_id_without_none(self, session):
        user_ids = session.scalars(
            select(User.id)
        ).all()

        return random.choice(user_ids)


    def fake_car_inject(self):
        fake = Faker()
        fake.add_provider(VehicleProvider)

        with Session(self.engine) as session:

            car_data = fake.vehicle_object()

            car = Car(
                user_id = self.fake_random_user_id_with_none(session),
                brand = car_data["Make"], 
                model = car_data["Model"],
                year =  car_data["Year"],
                license_plate = fake.bothify(text="???###").upper(),
            )

            session.add(car)
            session.commit()

    def fake_address_inject(self):

        fake = Faker("es_ES")

        with Session(self.engine) as session:
            address = Address(
                user_id = self.fake_random_user_id_without_none(session),
                full_address = fake.address(),
            )

            session.add(address)
            session.commit()




