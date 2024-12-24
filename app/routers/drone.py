from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/drones/", response_model=schemas.Drone)
def create_drone(drone: schemas.DroneCreate, db: Session = Depends(database.get_db)):
    return crud.create_drone(db, drone)
