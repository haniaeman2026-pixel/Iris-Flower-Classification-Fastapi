# ==========================================
# Iris Classification Model Training
# ==========================================

# Import Libraries
import pandas as pd
import joblib

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ==========================================
# Load Iris Dataset
# ==========================================

iris = load_iris()

X = iris.data
y = iris.target

# Convert dataset into DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df["target"] = y

print("=" * 50)
print("First Five Rows of Dataset")
print("=" * 50)
print(df.head())

# ==========================================
# Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ==========================================
# Logistic Regression Model
# ==========================================

print("\nTraining Logistic Regression Model...")

lr_model = LogisticRegression(max_iter=200)

lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_predictions)

print(f"Logistic Regression Accuracy : {lr_accuracy:.2%}")

# ==========================================
# Random Forest Model
# ==========================================

print("\nTraining Random Forest Model...")

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_predictions)

print(f"Random Forest Accuracy : {rf_accuracy:.2%}")

# ==========================================
# Select Best Model
# ==========================================

if rf_accuracy >= lr_accuracy:
    best_model = rf_model
    best_model_name = "Random Forest"
    best_accuracy = rf_accuracy
else:
    best_model = lr_model
    best_model_name = "Logistic Regression"
    best_accuracy = lr_accuracy

# ==========================================
# Save Best Model
# ==========================================

joblib.dump(best_model, "iris_model.pkl")

print("\n" + "=" * 50)
print("Best Model Selected")
print("=" * 50)
print(f"Model Name : {best_model_name}")
print(f"Accuracy   : {best_accuracy:.2%}")
print("Model saved successfully as 'iris_model.pkl'")
print("=" * 50)