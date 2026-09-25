from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

metadata_obj = MetaData(schema="cars_inventory")


address = Table(
    "Address",
    metadata_obj,
    Column("id", Integer,primary_key=True),
    Column("user_id", Integer, ForeignKey("Users.id"),nullable=False),
    Column("full_address", String(80), nullable=False),
)

automoviles = Table(
    "Automoviles",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("User_id", Integer, ForeignKey("Users.id"), nullable=True),
    Column("brand", String(30), nullable=False),
    Column("model", String(30), nullable=False),
    Column("year", Integer, nullable=False),
    Column("license_plate", String(6), nullable=False),
)

users_table = Table(
    "Users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_name", String(30), nullable=False),
    Column("full_name", String(60), nullable=False),
    Column("email", String(40)),
)