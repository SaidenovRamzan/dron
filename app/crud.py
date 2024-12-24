from sqlalchemy.orm import Session
from . import models, schemas

def get_drone(db: Session, drone_id: int):
    return db.query(models.Drone).filter(models.Drone.id == drone_id).first()

def create_drone(db: Session, drone: schemas.DroneCreate):
    db_drone = models.Drone(**drone.dict())
    db.add(db_drone)
    db.commit()
    db.refresh(db_drone)
    return db_drone

def create_image(db: Session, image: schemas.ImageCreate):
    db_image = models.ImageData(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
