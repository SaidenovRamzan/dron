from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas, database
import shutil
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from io import BytesIO


img_router = APIRouter()

# Загрузка модели
model = load_model("./fire_detection_model.keras")

# Функция для предсказания
def predict_fire(image_bytes: BytesIO):
    # Загрузка изображения из памяти
    img = load_img(image_bytes, target_size=(150, 150))  # Используйте размер, который использовался при обучении
    img_array = img_to_array(img) / 255.0  # Нормализация изображения
    img_array = np.expand_dims(img_array, axis=0)  # Добавление размерности для батча

    # Получение предсказания
    prediction = model.predict(img_array)
    return "Fire Detected" if prediction[0][0] > 0.3 else "No Fire"


@img_router.post("/images/")
def upload_image(
    image: schemas.ImageCreate,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(database.get_db),
):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    image.image_path = file_path
    return crud.create_image(db, image)


# Эндпоинт для обработки изображения
@img_router.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Чтение файла как байтов (в памяти)
    image_bytes = BytesIO(await file.read())

    # Предсказание
    result = predict_fire(image_bytes)
    return {"result": result}