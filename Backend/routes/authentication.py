from fastapi import APIRouter, Depends, HTTPException, status, Form
import schemas
from sqlalchemy.orm import Session
import services
import models
from datetime import timedelta
from . import token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



router = APIRouter(
    tags=['Authentication']
)

# @router.post('/login')
# def login(request: schemas.Login = Depends(), db: Session = Depends(services.get_db)):
#     if request.role=="Producer":
#         try:
#             username = int(request.username)
#             user = db.query(models.Producers).filter(models.Producers.phone == username).first()
#             access_token = token.create_access_token(data={"sub": user.phone, "role":request.role})
#         except ValueError:
#             user = db.query(models.Producers).filter(models.Producers.email == request.username).first()
#             access_token = token.create_access_token(data={"sub": user.email, "role":request.role})
#         if not user:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
        
#         if not services.Hash.verify(user.pass_hash,request.password):
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect pwd")
        
#     elif request.role=="Consumer":
#         try:
#             int(request.username)
#             user = db.query(models.Consumers).filter(models.Consumers.phone == request.username).first()
#             access_token = token.create_access_token(data={"sub": user.phone, "role":request.role})
#         except ValueError:
#             user = db.query(models.Consumers).filter(models.Consumers.email == request.username).first()
#             access_token = token.create_access_token(data={"sub": user.email, "role":request.role})
#         user = db.query(models.Consumers).filter(models.Consumers.email == request.username).first()
#         if not user:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
        
#         if not services.Hash.verify(user.pass_hash,request.password):
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect pwd")
            
#     return {"access_token": access_token, "token_type": "bearer"}


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(services.get_db)):
    try:
        username = int(request.username)
        user = db.query(models.Producers).filter(models.Producers.phone == username).first()
        access_token = token.create_access_token(data={"sub": user.phone})
    except ValueError:
        user = db.query(models.Producers).filter(models.Producers.email == request.username).first()
        access_token = token.create_access_token(data={"sub": user.email})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    if not services.Hash.verify(user.pass_hash,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect pwd")
            
    return {"access_token": access_token, "token_type": "bearer"}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token.verify_token(token, credentials_exception)
    