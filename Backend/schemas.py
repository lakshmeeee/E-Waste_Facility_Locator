import datetime as dt
from pydantic import BaseModel


class CreateProducer(BaseModel):
    pname: str
    category: str
    email: str
    pass_hash: str
    phone: str
    address: str
    state: str
    pincode: str

    class Config:
        orm_mode = True


class ShowProducer(BaseModel):
    pname: str
    category: str
    email: str
    phone: str
    address: str
    state: str
    pincode: str
    credits: int
    date_created: dt.datetime

    class Config:
        orm_mode = True



class CreateConsumer(BaseModel):
    cname: str
    email: str
    pass_hash: str
    phone: str
    category: str
    epr_id: str
    address: str
    state: str
    pincode: int
    gmap_link: str
    start_time: dt.time
    end_time: dt.time
    doorstep_coll: bool

    class Config:
        orm_mode = True


class ShowConsumerBackend(BaseModel):
    cid: int
    cname: str
    email: str
    pass_hash: str
    phone: str
    category: str
    epr_id: str
    address: str
    state: str
    pincode: int
    gmap_link: str
    start_time: dt.time
    end_time: dt.time
    doorstep_coll: bool
    latitude: str
    longitude: str
    date_created: dt.datetime

    class Config:
        orm_mode = True


class ShowConsumer(BaseModel):
    cname: str
    email: str
    phone: str
    category: str
    address: str
    state: str
    pincode: int
    gmap_link: str
    start_time: dt.time
    end_time: dt.time
    doorstep_coll: bool

    class Config:
        orm_mode = True


class ConsWithDist(BaseModel):
    cname: str
    email: str
    phone: str
    category: str
    address: str
    state: str
    pincode: int
    gmap_link: str
    start_time: dt.time
    end_time: dt.time
    doorstep_coll: bool
    distance: float

    class Config:
        orm_mode = True



class Login(BaseModel):
    role: str
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
