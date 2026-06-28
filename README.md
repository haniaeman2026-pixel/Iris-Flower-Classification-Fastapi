.

🌸 Iris Flower Classification API
High-Performance Machine Learning API using FastAPI
 Overview

This project is a production-style Machine Learning API built with FastAPI that predicts the species of an Iris flower based on its morphological measurements.

The system uses a trained Scikit-learn classification model and exposes predictions through a fast, scalable REST API.

It is designed as a beginner-to-intermediate ML deployment project demonstrating end-to-end workflow:
Data → Training → Serialization → API → Inference

 Objective

To classify Iris flowers into one of three species:

🌼 Setosa
🌼 Versicolor
🌼 Virginica

using supervised machine learning techniques.

 Model Information

Algorithm: Logistic Regression / Decision Tree / Random Forest
Dataset: Iris Dataset (Scikit-learn built-in)
Problem Type: Multi-class Classification
Input Features:
Sepal Length (cm)
Sepal Width (cm)
Petal Length (cm)
Petal Width (cm)
Output: Predicted Iris Species

 Tech Stack

Layer	Technology
API Framework	FastAPI
ML Library	Scikit-learn
Language	Python
Model Storage	Joblib / Pickle
Server	Uvicorn

 Project Structure
iris-classification-api/
│
├── app/
│   ├── main.py            # FastAPI application entry point
│   ├── schema.py          # Pydantic request validation
│   ├── model.pkl          # Trained ML model
│   └── utils.py          # Helper functions (optional)
│
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── training.ipynb         # Model training notebook
🚀 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/iris-classification-api.git
cd iris-classification-api
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Application

Start the FastAPI server using Uvicorn:

uvicorn app.main:app --reload
🌐 API Access
Service	URL
API Root	http://127.0.0.1:8000
Swagger UI	http://127.0.0.1:8000/docs
ReDoc	http://127.0.0.1:8000/redoc
📤 API Endpoint
🔹 Predict Iris Species

POST /predict

📥 Request Body
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
📤 Response
{
  "prediction": "setosa",
  "confidence": 0.98
}
🔄 Example Usage (Python Client)
import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "sepal_length": 6.2,
    "sepal_width": 3.4,
    "petal_length": 5.4,
    "petal_width": 2.3
}

response = requests.post(url, json=data)

print(response.json())

 Key Features
High-speed inference using FastAPI
 ML model integration using Scikit-learn
 Clean modular architecture
 Input validation using Pydantic
 Auto-generated API documentation (Swagger)
 Production-ready structure
 Performance
Accuracy: ~95%+ (depends on model selection)
Response Time: < 100ms (local environment)
Lightweight & scalable API design

 Testing

You can test the API using:

Swagger UI → /docs
Postman
Python requests
cURL

 Future Enhancements
 Deploy on Render / AWS / Railway
 Add Authentication (JWT)
 Add logging & monitoring
 Try advanced models (XGBoost, SVM)
 Add frontend UI (React / Streamlit)
 Author

Hania Eman
AI / Machine Learning Developer 