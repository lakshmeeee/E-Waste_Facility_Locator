from fastapi import FastAPI, HTTPException, Depends, security, Query
from typing import List, Annotated, Optional
import models as models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import services as services
import schemas as schemas
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import producer, authentication, consumer
# from locator import nearby_facility

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(producer.router)
app.include_router(authentication.router)
app.include_router(consumer.router)

@app.get("/")
async def root():
    return {"message": "Hello World"} 





# Configure CORS to allow requests from your React app's domain
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/location")
# async def process_location(
#     latitude: float = Query(..., description="The latitude of the location"),
#     longitude: float = Query(..., description="The longitude of the location"),
#     zipcode: int = Query(..., description="The zipcode of the location"),
# ):
#     # Process the location data here (e.g., perform some calculations)
#     result = nearby_facility(latitude, longitude, zipcode)
#     return result


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
