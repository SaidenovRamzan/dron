from pydantic import BaseModel
from datetime import datetime

class DroneBase(BaseModel):
    name: str
    status: str

class DroneCreate(DroneBase):
    pass

class Drone(DroneBase):

    class Config:
        orm_mode = True

class ImageBase(BaseModel):
    drone_id: int
    latitude: float
    longitude: float
    timestamp: datetime

class ImageCreate(ImageBase):
    pass

class Image(ImageBase):
    id: int
    image_path: str

    class Config:
        orm_mode = True
