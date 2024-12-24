from fastapi import FastAPI
import uvicorn
from app.database import create_tables
from app.routers import img_router, dron_router
from app.database import Base, engine


async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)

# Подключение роутеров
app.include_router(dron_router, prefix="/api")
app.include_router(img_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)