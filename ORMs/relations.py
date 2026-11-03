from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "Users"
    __table_args__ = {"schema":"cars_inventory"}

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(30))
    full_name: Mapped[str] = mapped_column(String(60))
    email: Mapped[str] = mapped_column(String(40))

    cars: Mapped[list["Car"]] = relationship(
        back_populates = "user"
    )
    addresses: Mapped[list["Address"]] = relationship(
        back_populates = "user"
    )

class Car(Base):
    __tablename__ = "cars"
    __table_args__ = {"schema":"cars_inventory"}

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(30))
    model: Mapped[str] = mapped_column(String(30))
    year: Mapped[int] = mapped_column(Integer)
    license_plate: Mapped[str] = mapped_column(String(6))
    
    user_id: Mapped[int | None] = mapped_column("User_id", ForeignKey("cars_inventory.Users.id"),
                                                nullable=True)

    user: Mapped["User | None"] = relationship(back_populates="cars")

class Address(Base):
    __tablename__ = "Address"
    __table_args__ = {"schema":"cars_inventory"}

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("cars_inventory.Users.id"))
    full_address: Mapped[str] = mapped_column(String(80))

    user: Mapped["User"] = relationship(back_populates="addresses")
