import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

# ===============================
# 1. PATH DATASET
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')

# ===============================
# 2. PARAMETER
# ===============================
IMG_SIZE = (224, 224)
BATCH_SIZE = 16        # dinaikkan agar training lebih stabil
EPOCHS = 30            # ditambah
NUM_CLASSES = 8        # anger, contempt, disgust, fear, happy, neutral, sad, surprise

print("Dataset path:", DATASET_DIR)

# ===============================
# 3. DATA AUGMENTATION (AMAN UNTUK WAJAH)
# ===============================
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    validation_split=0.2
)

train_generator = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_generator = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# ===============================
# 4. MODEL: MOBILENETV2 + FINE TUNING
# ===============================
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

# Fine-tuning: bekukan layer awal
base_model.trainable = True
for layer in base_model.layers[:100]:
    layer.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.4)(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.3)(x)

predictions = Dense(NUM_CLASSES, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# ===============================
# 5. COMPILE
# ===============================
model.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# ===============================
# 6. CALLBACKS (BIAR TIDAK OVERFIT)
# ===============================
callbacks = [
    EarlyStopping(
        monitor='val_loss',
        patience=7,
        restore_best_weights=True
    ),
    ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.3,
        patience=3,
        min_lr=1e-6
    )
]

# ===============================
# 7. TRAINING
# ===============================
print("\n🚀 Memulai Training...\n")

history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=val_generator,
    callbacks=callbacks,
    verbose=1
)

# ===============================
# 8. SIMPAN MODEL
# ===============================
model.save('emotion_model.h5')
print("\n✅ Training selesai!")
print("📁 Model disimpan sebagai: emotion_model.h5")
