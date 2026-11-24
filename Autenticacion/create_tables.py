from sqlalchemy import MetaData, Table, Column, Integer, Numeric, Date, String, ForeignKey
from connect_db import MakeConectionDb

metadata_obj = MetaData(schema="fruit_shop_inventory")

fruit_table = Table(
    "Fruit",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("fruit_name",String(30), nullable=False),
    Column("price",Numeric(10,2), nullable=False),
    Column("delivery_date", Date, nullable=False),
    Column("stock", Integer, default=0, nullable=False),
)

user_table = Table(
    "Users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_name", String(30), nullable=False),
    Column("email", String(50), nullable=False),
    Column("password", String, nullable= False),
    Column("role", String(15), nullable=False),
)


invoices_table = Table(
    "Invoices",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("Users.id"), nullable=False),
    Column("fruit_id", Integer, ForeignKey("Fruit.id"), nullable=False),
    Column("quantity", Integer, default=0, nullable=False),
    Column("price", Numeric(10,2), nullable=False),
    Column("invoices_date", Date, nullable=False),
)

db = MakeConectionDb()

metadata_obj.create_all(db.engine)

print("Tables created successfully!")