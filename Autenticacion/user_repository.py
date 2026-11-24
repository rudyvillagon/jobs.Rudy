from sqlalchemy import insert, select
from connect_db import MakeConectionDb
from create_tables import user_table


class UserRepository:
    def __init__(self, engine):
        self.engine = engine

    def create(self, user_name, password):
        stmt = (
            insert(user_table)
            .values(user_name=user_name, password=password)
            .returning(user_table.c.id)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.first()

    def get_by_credentials(self, user_name, password):
        stmt = select(user_table).where(
            user_table.c.user_name == user_name,
            user_table.c.password == password,
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            return result.first()

    def get_by_id(self, user_id):
        stmt = select(user_table).where(user_table.c.id == user_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            return result.first()

db = MakeConectionDb()
user_repository = UserRepository(db.engine)