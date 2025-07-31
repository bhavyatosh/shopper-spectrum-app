import os
import joblib

def load_kmeans_model():
    """
    Loads the trained KMeans model and scaler.
    Returns:
        model: Trained KMeans clustering model
        scaler: Scaler used during model training
    """
    model_path = os.path.join("model", "kmeans_model.pkl")
    scaler_path = os.path.join("model", "scaler.pkl")

    if not os.path.exists(model_path):
        raise FileNotFoundError("❌ KMeans model file not found.")
    if not os.path.exists(scaler_path):
        raise FileNotFoundError("❌ Scaler file not found.")

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    return model, scaler
