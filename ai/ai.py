import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Настройка путей
dataset_path = "path_to_dataset"

# Подготовка данных
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_gen = datagen.flow_from_directory(
    dataset_path, 
    target_size=(150, 150), 
    batch_size=32, 
    class_mode='binary', 
    subset='training'
)
val_gen = datagen.flow_from_directory(
    dataset_path, 
    target_size=(150, 150), 
    batch_size=32, 
    class_mode='binary', 
    subset='validation'
)

# Создание модели
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Обучение
model.fit(train_gen, validation_data=val_gen, epochs=10)

# Сохранение модели
model.save("fire_detection_model.keras") 
