import os
import json
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from preprocessing import create_generators

# Paths
TRAIN_DIR = 'Dataset/Train'
TEST_DIR = 'Dataset/Test'
MODEL_SAVE_PATH = 'dogbreed.h5'

# Parameters
IMAGE_SIZE = [224, 224]
BATCH_SIZE = 32
EPOCHS = 1 # Reduced for testing

def build_model(num_classes):
    # Load VGG19 without top layers
    vgg = VGG19(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

    # Freeze VGG layers
    for layer in vgg.layers:
        layer.trainable = False

    # Add custom layers
    x = Flatten()(vgg.output)
    prediction = Dense(num_classes, activation='softmax')(x)

    # Create model
    model = Model(inputs=vgg.input, outputs=prediction)
    
    # Compile model
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )
    
    return model

def main():
    # Check if data directories exist
    # Check if data directories exist
    if not os.path.exists(TRAIN_DIR):
        print(f"Data directory not found: {TRAIN_DIR}")
        return

    # Create generators
    train_generator, val_generator = create_generators(TRAIN_DIR, TEST_DIR, target_size=tuple(IMAGE_SIZE), batch_size=BATCH_SIZE)
    
    num_classes = len(train_generator.class_indices)
    print(f"Detected {num_classes} classes.")

    # Save class indices
    with open('class_indices.json', 'w') as f:
        json.dump(train_generator.class_indices, f)
    print("Class indices saved to class_indices.json")

    # Build model
    model = build_model(num_classes)
    model.summary()

    # Train model
    print("Starting training...")
    history = model.fit(
        train_generator,
        validation_data=val_generator,
        epochs=EPOCHS,
        steps_per_epoch=10, # Limiting steps for faster verification
        validation_steps=10 # Limiting steps for faster verification
    )

    # Save model
    model.save(MODEL_SAVE_PATH)
    print(f"Model saved to {MODEL_SAVE_PATH}")

if __name__ == "__main__":
    main()
