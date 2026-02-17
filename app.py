import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model
MODEL_PATH = 'dogbreed.h5'
model = None

import json

# Load class names from the JSON file generated during training
# Expecting class_indices.json to be in the same directory
CLASS_INDICES_PATH = 'class_indices.json'
CLASS_NAMES = None

def load_class_names():
    global CLASS_NAMES
    if os.path.exists(CLASS_INDICES_PATH):
        with open(CLASS_INDICES_PATH, 'r') as f:
            class_indices = json.load(f)
            # Invert the dictionary: { 'breed': index } -> { index: 'breed' }
            # Ensure indices are integers for lookup
            CLASS_NAMES = {v: k for k, v in class_indices.items()}
            print(f"Loaded {len(CLASS_NAMES)} classes from {CLASS_INDICES_PATH}")
    else:
        print(f"Warning: {CLASS_INDICES_PATH} not found. Predictions might be incorrect or fail.")
        CLASS_NAMES = {}

load_class_names() 

def load_my_model():
    global model
    if os.path.exists(MODEL_PATH):
        try:
            model = load_model(MODEL_PATH)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            model = None
    else:
        print("Model file not found. Please train the model first.")
        model = None

load_my_model()

def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)
    return x

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            if model:
                # Prediction
                img_data = prepare_image(file_path)
                preds = model.predict(img_data)
                pred_index = np.argmax(preds)
                # Ensure CLASS_NAMES is loaded and has the index
                if CLASS_NAMES and pred_index in CLASS_NAMES:
                    pred_class = CLASS_NAMES[pred_index]
                else:
                    pred_class = f"Unknown Class (Index: {pred_index})"
                
                return render_template('output.html', image_file=filename, prediction=pred_class)
            else:
                return render_template('predict.html', error="Model not loaded. Please train the model first.")
    return render_template('predict.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
