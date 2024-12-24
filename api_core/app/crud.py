from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas


async def get_drone(db: AsyncSession, drone_id: int):
    result = await db.execute(select(models.Drone).where(models.Drone.id == drone_id))
    return result.scalars().first()


async def create_drone(db: AsyncSession, drone: schemas.DroneCreate):
    db_drone = models.Drone(**drone.dict())
    db.add(db_drone)
    await db.commit()  # Асинхронный вызов commit
    await db.refresh(db_drone)  # Асинхронный вызов refresh
    return db_drone

async def create_image(db: AsyncSession, image: schemas.ImageCreate):
    db_image = models.ImageData(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
