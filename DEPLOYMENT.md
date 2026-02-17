# Deployment Guide

You asked about deploying to **Vercel**.

## ❌ Why Vercel is not recommended for this project
Vercel is optimized for frontend frameworks (Next.js, React) and small serverless functions.
- **Size Limit**: Vercel has a hard limit of **250MB** (unzipped) for Serverless Functions.
- **Your Project**:
    - `tensorflow` library: ~500MB+
    - `dogbreed.h5` model: ~116MB
    - **Total**: >600MB
- **Result**: The deployment will fail during the build process because it exceeds the size limit.

## ✅ Recommended Alternative: Render.com
Render is a cloud platform that supports full Docker/Python web services and has a generous free tier. It handles large libraries like TensorFlow much better.

### Steps to Deploy on Render

1.  **Prepare the Project** (I will do this for you):
    - Add `gunicorn` to `requirements.txt` (Production server).
    - Create a `Procfile` (tells Render how to run the app).
    - Push these changes to GitHub.

2.  **Create Service on Render**:
    - Sign up at [dashboard.render.com](https://dashboard.render.com/).
    - Click **New +** -> **Web Service**.
    - Connect your GitHub repository: `Uday-Kiran-06/Dog_Breed_Identification`.
    - **Name**: `dog-breed-prediction` (or similar).
    - **Runtime**: `Python 3`.
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `gunicorn app:app` (This will be auto-detected from the Procfile).
    - **Instance Type**: Select **Free**.
    - Click **Create Web Service**.

3.  **Wait for Build**:
    - Render will install TensorFlow and your dependencies. This might take 5-10 minutes.
    - Once done, you will get a URL like `https://dog-breed-prediction.onrender.com`.

## Note on "Development Server" Warning
The warning `WARNING: This is a development server` in your local terminal is normal when running `python app.py`.
- Locally, it's fine.
- In production (Render), we use `gunicorn` (as configured in the Procfile) to remove this warning and handle requests efficiently.
