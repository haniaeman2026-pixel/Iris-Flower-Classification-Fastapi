# ==========================================================
# Iris Flower Prediction API
# Developed By: Hania Eman
# Framework: FastAPI
# ==========================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np

# ==========================================================
# FastAPI Configuration
# ==========================================================

app = FastAPI(
    title="Iris Flower Prediction API",
    description="A REST API built with FastAPI to predict Iris Flower Species using a trained Machine Learning model.",
    version="2.0.0"
)

# ==========================================================
# Load Trained Model
# ==========================================================

try:
    model = joblib.load("iris_model.pkl")
    print("✅ Model Loaded Successfully")
except Exception as e:
    raise RuntimeError(f"Error Loading Model: {e}")

# ==========================================================
# Flower Classes
# ==========================================================

CLASS_NAMES = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

# ==========================================================
# Input Schema
# ==========================================================

class IrisInput(BaseModel):
    sepal_length: float = Field(..., example=5.1)
    sepal_width: float = Field(..., example=3.5)
    petal_length: float = Field(..., example=1.4)
    petal_width: float = Field(..., example=0.2)

# ==========================================================
# Response Schema
# ==========================================================

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float

# ==========================================================
# Home Endpoint
# ==========================================================

@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Welcome to Iris Flower Prediction API",
        "status": "Running Successfully",
        "developer": "Hania Eman",
        "framework": "FastAPI",
        "model": "Machine Learning - Iris Classification"
    }

# ==========================================================
# Prediction Endpoint
# ==========================================================

@app.post(
    "/predict",
    response_model=PredictionResponse,
    tags=["Prediction"]
)
def predict(data: IrisInput):

    try:

        # Input Data
        input_data = np.array([[
            data.sepal_length,
            data.sepal_width,
            data.petal_length,
            data.petal_width
        ]])

        # Prediction
        prediction = int(model.predict(input_data)[0])

        # Confidence Score
        confidence = 100.0

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]
            confidence = round(float(np.max(probabilities) * 100), 2)



        # Return Response
        return PredictionResponse(
            prediction=CLASS_NAMES[prediction],
            confidence=confidence
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction Error: {str(e)}"
        )

# ==========================================================
# Health Check Endpoint
# ==========================================================

@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "Healthy",
        "API": "Running",
        "Model": "Loaded Successfully"
    }