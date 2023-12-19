from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time, DateTime, Date, func
from database import Base
from sqlalchemy.orm import relationship
import passlib.hash as hash
import datetime as dt


class Producers(Base):
    __tablename__ = 'producers'

    pid = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True, server_default=func.coalesce(func.max(id), 0))
    pname = Column(String, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    pass_hash = Column(String, index=True, nullable=False) #hashed 
    phone = Column(String, index=True, nullable=False)
    address = Column(String, index=True, nullable=False)
    state = Column(String, index=True, nullable=False)
    pincode = Column(String, index=True, nullable=False)
    credits = Column(Integer, index=True, nullable=False, default=0)
    latitude = Column(String, index=True, nullable=False)
    longitude = Column(String, index=True, nullable=False)
    date_created = Column(DateTime, default=dt.datetime.utcnow) #ETL Audit Date
    
    prod = relationship("Transaction", back_populates="prod")


class Consumers(Base):
    __tablename__ = 'consumers'

    cid = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    cname = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    pass_hash = Column(String, index=True, nullable=False)
    phone = Column(String, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    epr_id = Column(String, index=True, nullable=False)
    address = Column(String, index=True, nullable=False)
    state = Column(String, index=True, nullable=False)
    pincode = Column(Integer, index=True, nullable=False)
    gmap_link = Column(String, index=True, nullable=False)
    start_time = Column(Time, index=True, nullable=False)
    end_time = Column(Time, index=True, nullable=False)
    doorstep_coll = Column(Boolean, index=True, nullable=False)
    latitude = Column(String, index=True, nullable=False)
    longitude = Column(String, index=True, nullable=False)
    date_created = Column(DateTime, default=dt.datetime.utcnow) #ETL Audit Date

    cons = relationship("Transaction", back_populates="cons")

    
class Products(Base):
    __tablename__ = 'products'

    did = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    dname = Column(String, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    brand_name = Column(String, index=True, nullable=False)
    model = Column(String, index=True, nullable=False)
    quantity = Column(Integer, index=True, nullable=False)
    condition = Column(String, index=True, nullable=False)
    date_created = Column(DateTime, default=dt.datetime.utcnow) #ETL Audit Date

    item = relationship("Transaction", back_populates="item")


class Transaction(Base):
    __tablename__ = 'transaction'

    tid = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    pid = Column(Integer, ForeignKey("producers.pid"))
    cid = Column(Integer, ForeignKey("consumers.cid"))
    did = Column(Integer, ForeignKey("products.did"))
    status = Column(String, index=True, nullable=False)
    delivery_pname = Column(String, index=True)
    delivery_phno = Column(String, index=True)
    created = Column(DateTime, index=True, default=dt.datetime.utcnow)
    response_date = Column(Date, index=True)
    date_created = Column(DateTime, default=dt.datetime.utcnow) #ETL Audit Date
    date_updated = Column(DateTime, default=dt.datetime.utcnow) #ETL Audit Date

    prod = relationship("Producers", back_populates="prod")
    cons = relationship("Consumers", back_populates="cons")
    item = relationship("Products", back_populates="item")