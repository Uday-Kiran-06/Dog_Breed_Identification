from tensorflow.keras.preprocessing.image import ImageDataGenerator

def create_generators(train_dir, test_dir, target_size=(224, 224), batch_size=32):
    """
    Creates ImageDataGenerators for training and validation.
    """
    # Train Data Generator with Augmentation and Validation Split
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.2 # Added validation split
    )

    # Load Train Data (Subset: training)
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    # Load Validation Data (Subset: validation)
    val_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )

    return train_generator, val_generator
