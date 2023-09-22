from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Time
from database import Base

class Producers(Base):
    __tablename__ = 'producers'

    uid = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False, unique=True)
    password = Column(String(length=50), index=True)
    phone = Column(String, index=True, nullable=False)
    address = Column(String, index=True, nullable=False)
    pincode = Column(String, index=True, nullable=False)

class Products(Base):
    __tablename__ = 'products'

    pid = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    pname = Column(String, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    man_yr = Column(Integer, index=True, nullable=False)
    working_or_not = Column(Boolean, index=True, nullable=False)
    uid = Column(Integer, ForeignKey("producers.uid"))
    cid = Column(Integer, ForeignKey("consumers.cid"))

class Consumers(Base):
    __tablename__ = 'consumers'

    cid = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    cname = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False)
    password = Column(String(length=50), index=True, nullable=False)
    phone = Column(String, index=True, nullable=False)
    consumer_or_recycler = Column(String, index=True, nullable=False)
    location = Column(String, index=True, nullable=False)
    operation_time = Column(Time, index=True, nullable=False)
    pincode = Column(Integer, index=True, nullable=False)

class Transaction(Base):
    __tablename__ = 'transaction'

    tid = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    pid = Column(Integer, ForeignKey("products.pid"))
    uid = Column(Integer, ForeignKey("producers.uid"))
    cid = Column(Integer, ForeignKey("consumers.cid"))
    status = Column(String, index=True, nullable=False)
    timestamp = Column(TIMESTAMP, index=True, nullable=False)