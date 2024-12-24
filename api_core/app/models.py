from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Drone(Base):
    __tablename__ = "drones"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, default="active")
    images = relationship("ImageData", back_populates="drone")

class ImageData(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    drone_id = Column(Integer, ForeignKey("drones.id"))
    image_path = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    timestamp = Column(DateTime)

    drone = relationship("Drone", back_populates="images")
