from fastapi import FastAPI
from .routers import drone, image
from .database import Base, engine

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключение роутеров
app.include_router(drone.router, prefix="/api")
app.include_router(image.router, prefix="/api")
