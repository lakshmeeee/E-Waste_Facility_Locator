from fastapi import APIRouter, Depends, HTTPException, status
import schemas
from sqlalchemy.orm import Session
import services
import models



router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(services.get_db)):
    if request.role=="Producer":
        try:
            username = int(request.username)
            user = db.query(models.Producers).filter(models.Producers.phone == username).first()
        except ValueError:
            user = db.query(models.Producers).filter(models.Producers.email == request.username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
        
        if not services.Hash.verify(user.pass_hash,request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect pwd")
        
    elif request.role=="Consumer":
        try:
            int(request.username)
            user = db.query(models.Consumers).filter(models.Consumers.phone == request.username).first()
        except ValueError:
            user = db.query(models.Consumers).filter(models.Consumers.email == request.username).first()
        user = db.query(models.Consumers).filter(models.Consumers.email == request.username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
        
        if not services.Hash.verify(user.pass_hash,request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect pwd")
            
    return user

