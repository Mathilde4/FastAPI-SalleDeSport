from sqlalchemy import Column, Integer, String, Date, Boolean, Float, ForeignKey, Enum
from .database import Base
from sqlalchemy.orm import relationship
import enum

class RoleEnum(str, enum.Enum):
    user = 'User'
    admin = 'Admin'

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key = True, index=True)
    last_name = Column(String)
    first_name = Column(String)
    registration_date = Column(Date)
    phone_number = Column(Integer)
    active_suscription = Column(Boolean, default=False)

    subscriptions = relationship("subscription", back_populates="customer", cascade="all, delete")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.user)
    

class Pack(Base):
    __tablename__ = "packs"
    id = Column(Integer, primary_key = True, index= True)
    offer_name = Column(String)
    duration_months = Column(Integer) 
    monthly_price = Column(Float)

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key = True, index= True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    pack_id = Column(Integer, ForeignKey("packs.id"))
    start_date = Column(Date)

    customer = relationship("customer", back_populates="subcriptions")
    pack = relationship("pack")
