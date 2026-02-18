# Dog Breed Prediction

This is a Flask-based web application that predicts the breed of a dog from an image using a deep learning model (TensorFlow/Keras).

![Home Page](assets/Home.png)

## Demo
**Project Demo:**https://drive.google.com/drive/folders/1lV609Zr0z2Xnj5H-aJGZNY78PsmQWGjP?usp=sharing

## Features

- **Upload Image:** Users can upload an image of a dog.
- **Breed Prediction:** The application processes the image and predicts the dog's breed using a pre-trained model.
- **User-Friendly Interface:** Simple and intuitive web interface.
- **Responsive Design:** Works on desktop and mobile devices.

## Technologies Used

- **Backend:** Python, Flask
- **Machine Learning:** TensorFlow, Keras, NumPy
- **Frontend:** HTML, CSS (Bootstrap/Tailwind - based on templates)
- **Image Processing:** Pillow, TensorFlow Keras Preprocessing

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd DOG_BREED_PREDICTION
    ```

2.  **Create and activate a virtual environment (optional but recommended):**

    - **Windows:**
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
    - **macOS/Linux:**
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**

    ```bash
    python app.py
    ```

2.  **Open your browser:**
    Go to `http://127.0.0.1:5000/`

3.  **Predict a Dog Breed:**
    - Click "Choose File" to upload a dog image.
    - Click "Predict" (or the appropriate button).
    - View the result on the output page.

## Project Structure

```
DOG_BREED_PREDICTION/
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── dogbreed.h5            # Pre-trained model file
├── class_indices.json     # Class indices mapping
├── preprocessing.py       # Image preprocessing utilities
├── train_model.py         # Script used for training the model
├── reorganize_dataset.py  # Utility for dataset organization
├── static/                # Static assets (CSS, JS, images)
├── templates/             # HTML templates
├── uploads/               # Directory for uploaded images
├── assets/                # Documentation assets
│   └── Home.png           # Screenshot of the home page
└── README.md              # Project documentation
```

## Troubleshooting

- **Model Not Found:** Ensure `dogbreed.h5` is in the root directory.
- **Class Indices:** Ensure `class_indices.json` is present for accurate label mapping.
- **Upload Folder:** The `uploads` folder is automatically created if it doesn't exist.

