from sqlalchemy import create_engine

class MakeConectionDb:

    def __init__(self):
        self.DB_URI = "postgresql+psycopg2://postgres:123456@localhost:5432/car_inventory"
        self.engine = create_engine(self.DB_URI, echo=True)

    def connect(self):
        try:
            connection = self.engine.connect()
            print( "Connection seccessful!")
            connection.close()

        except Exception as e:
            print("Connection failed:", e)