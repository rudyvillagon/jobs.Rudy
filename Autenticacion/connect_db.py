from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

class MakeConectionDb:

    def __init__(self):
        self.DB_URI = "postgresql+psycopg2://postgres:123456@localhost:5432/fruit_shop_inventory"
        self.engine = create_engine(self.DB_URI, echo=True, connect_args={"options": "-c client_encoding=UTF8"})

    def connect(self):
        try:
            with self.engine.connect() as connection:
                print( "Connection seccessful!")
                return True

        except SQLAlchemyError as e:
            print(f"Connection_error: {e}")
            return False


    def close(self):
            self.engine.dispose()
