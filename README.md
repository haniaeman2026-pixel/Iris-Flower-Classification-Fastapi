#  Iris Classification API

> **A production-ready Machine Learning REST API built with FastAPI for Iris flower classification using Scikit-learn, featuring automatic API documentation (Swagger) and an interactive Streamlit frontend.**

---

##  Project Overview

The **Iris Classification API** is a Machine Learning project that predicts the species of an Iris flower using its morphological measurements.

The project demonstrates an end-to-end ML workflow:

**Data Collection → Model Training → Model Serialization → FastAPI Deployment → Streamlit Frontend → Prediction**

This project was developed using **Python**, **FastAPI**, **Scikit-learn**, and **Streamlit** following REST API principles.

---

##  Objectives

* Build a REST API using FastAPI
* Integrate a trained Machine Learning model
* Validate user input using Pydantic
* Generate automatic API documentation
* Create an interactive frontend using Streamlit
* Demonstrate a complete ML deployment workflow

---

##  Predicted Classes

* Setosa
* Versicolor
* Virginica

---

#  Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| FastAPI      | REST API Framework   |
| Scikit-learn | Machine Learning     |
| Streamlit    | Frontend Interface   |
| Joblib       | Model Serialization  |
| NumPy        | Numerical Computing  |
| Pydantic     | Input Validation     |
| Uvicorn      | ASGI Server          |

---

#  Project Structure

```text
iris-classification-api/
│
├── app.py                # FastAPI Application
├── train_model.py        # Model Training Script
├── iris_model.pkl        # Trained ML Model
├── streamlit_app.py      # Streamlit Fronten
├── requirements.txt      # Dependencies
├── README.md             # Project Documentation
└── screenshots/          # Project Screenshots (Optional)
```

---

#  Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/iris-classification-api.git
cd iris-classification-api
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI

```bash
uvicorn app:app --reload
```

API will be available at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# ▶️ Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

#  API Endpoint

## POST /predict

### Request

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Response

```json
{
  "prediction": "Setosa",
  "confidence": 99.87
}
```

---

#  Features

* Fast Machine Learning Inference
* RESTful API using FastAPI
* Input Validation with Pydantic
* Automatic Swagger Documentation
* Health Check Endpoint
* Interactive Streamlit Frontend
* Production-style Project Structure
* Clean & Readable Code
* Easy Deployment

---

#  Testing

The API can be tested using:

* Swagger UI
* Postman
* Python Requests
* cURL

---

#  Performance

* Accuracy: **95%+**
* Lightweight REST API
* Fast Prediction Response
* Low Memory Usage

---

#  Future Improvements

* Docker Support
* JWT Authentication
* Logging & Monitoring
* Cloud Deployment (Render / Railway / AWS)
* CI/CD Pipeline
* Unit Testing

---

#  Author

**Hania Eman**

AI & Machine Learning Developer

---

