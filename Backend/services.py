from fastapi import FastAPI
from sqlalchemy.orm import Session
import passlib.hash as hash
import database as database
import schemas as schemas
import datetime as dt
import models as models
import math
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from passlib.context import CryptContext


def create_database():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
async def get_user_by_email(email: str, db: Session):
    return db.query(models.Producers).filter(models.Producers.email == email).first()

async def create_user(user: schemas.CreateProducer, db: Session):
    user_obj = models.Producers(
        email=user.email, pass_hash=user.pass_hash,
        pname=user.pname, category=user.category,
        phone=user.phone, address=user.address,
        state=user.state, pincode=user.pincode,
        latitude=user.latitude, longitude=user.longitude
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

def distance(lat1, lon1, lat2, lon2, pincode):
    if pincode!=0:
        lat1, lon1 = find_lat_lon(pincode)
    return haversine_distance(lat1, lon1, lat2, lon2)



def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))

    # Radius of the Earth in kilometers
    radius = 6371.0  # Earth's radius in km

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = radius * c

    return distance


def find_lat_lon(pincode):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(pincode)
    return getLoc.latitude, getLoc.longitude

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def encrypt(password: str):
        return pwd_cxt.hash(password)
    def verify(hashed_password: str, plain_password: str):
        return pwd_cxt.verify(plain_password,hashed_password)
