# AI Model Deployment: Classification & Regression with Postman API

This repository provides a comprehensive guide to deploying machine learning models for both classification and regression tasks using Django and Flask frameworks. The deployment enables interaction with the models through GET and POST requests via Postman, making it easily accessible for testing and integration into applications.

## Overview

The deployment setup includes:
- **Django and Flask Scripts:** Python scripts to set up web servers that host the models.
- **Model Pickle (`.pkl`) Files:** Serialized versions of the trained classification and regression models.
- **Jupyter Notebooks:** Notebooks containing the model training process, evaluation, and instructions for use.
- **Screenshots:** Visual guides for setting up and using the Postman API with our endpoints.

## Directory Structure

```plaintext
project_root/
│
├── django_app/               # Django project files
│   ├── model_deployment/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py         # Model definitions
│   │   ├── tests.py
│   │   ├── views.py          # Views for handling requests
│   │
│   ├── project_name/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py       # Django settings
│   │   ├── urls.py           # Project URL definitions
│   │   └── wsgi.py
│   └── manage.py
│
├── flask_app/                # Flask application files
│   ├── app.py                # Main Flask application script
│   ├── requirements.txt      # Python dependencies
│   ├── models/               # Folder for storing .pkl model files
│
├── notebooks/                # Jupyter notebooks for models
│   ├── classification.ipynb
│   ├── regression.ipynb
│
├── screenshots/              # Tutorial screenshots
│   ├── postman_setup.png
│   ├── api_call_example.png
│
└── README.md
```

## Setup

1. **Install Dependencies:**
   - Ensure Python 3.6+ is installed.
   - Install requirements: `pip install -r flask_app/requirements.txt` for Flask, and similarly for Django if required.

2. **Running the Flask App:**
   - Navigate to the `flask_app` directory.
   - Run `python app.py` to start the Flask server.

3. **Running the Django App:**
   - Navigate to the Django project root.
   - Run `python manage.py runserver` to start the Django server.

4. **Postman Configuration:**
   - Import the provided Postman collection or configure manually using the screenshots as a guide.

## Usage

### Classification Model

- **GET Request:** Use to fetch predictive model details or health check.
- **POST Request:** Send a JSON payload with the input features to receive a classification prediction.

Example Payload for Classification:
```json
{
  "feature1": value1,
  "feature2": value2,
  ...
}
```

### Regression Model

- **GET Request:** Use to retrieve model metadata or verify server status.
- **POST Request:** Submit a JSON with input variables to get a regression output.

Example Payload for Regression:
```json
{
  "feature1": value1,
  "feature2": value2,
  ...
}
```

## Screenshots
![screenshot](https://github.com/figo2001/Model-Deployment-using-Postman-API/assets/78696850/61ddc998-6d50-4647-9eef-fc763daf8ecf)
![screenshot 1](https://github.com/figo2001/Model-Deployment-using-Postman-API/assets/78696850/8d8258fa-5880-4f0c-a5e0-0e610c41e615)




## Note

Ensure your model `.pkl` files are placed in the appropriate directories (`django_app` or `flask_app/models`) and are correctly referenced in the script files.

## Conclusion

This setup guide outlines how to deploy classification and regression models using Django and Flask, and how to interact with them through Postman API calls. It's a foundational step towards integrating machine learning capabilities into your applications.
