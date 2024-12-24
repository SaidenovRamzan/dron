from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas, database

dron_router = APIRouter()

@dron_router.post("/drones/", response_model=schemas.Drone)
async def create_drone(drone: schemas.DroneCreate, db: AsyncSession = Depends(database.get_db)):
    return await crud.create_drone(db, drone)

@dron_router.get("/drones/", response_model=schemas.Drone)
async def get_drone(db: AsyncSession = Depends(database.get_db)):
    return await crud.get_drone(db, 1)
