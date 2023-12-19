import schemas
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.encoders import jsonable_encoder
import services

from models import Consumers

router = APIRouter(
    tags = ["Consumers"]
)

@router.get("/consumer/all_consumers", response_model=List[schemas.ShowConsumerBackend])
def all(db: Session = Depends(services.get_db)):
    consumers = db.query(Consumers).all()
    return consumers


@router.post("/consumer/consumer_signup")
async def create_user(
    request: schemas.CreateConsumer, db: Session = Depends(services.get_db)
):
    db_user = db.query(Consumers).filter(Consumers.email == request.email).first()
    
    if db_user:
        raise HTTPException(status_code=400, detail="Email Already Exists")
    
    lat,lon = services.find_lat_lon(request.pincode)

    user_obj = Consumers(
        email=request.email, pass_hash=services.Hash.encrypt(request.pass_hash),
        cname=request.cname, category=request.category,
        epr_id=request.epr_id, gmap_link=request.gmap_link,
        phone=request.phone, address=request.address,
        state=request.state, pincode=request.pincode,
        start_time=request.start_time, end_time=request.end_time,
        doorstep_coll=request.doorstep_coll,
        latitude=lat, longitude=lon
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj