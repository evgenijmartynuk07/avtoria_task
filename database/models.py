from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String)
    title = Column(String)
    price_usd = Column(Integer)
    odometer = Column(Integer)
    username = Column(String, nullable=True)
    phone_number = Column(BigInteger, nullable=True)
    image_url = Column(String, nullable=True)
    images_count = Column(Integer, nullable=True)
    car_number = Column(String, nullable=True)
    car_vin = Column(String, nullable=True)
    datetime_found = Column(DateTime(timezone=True), server_default=func.now())
