import os
import joblib
class Predictor:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(BASE_DIR, "../../saved_models/best_model.pkl")
        self.model = joblib.load(model_path)
    def predict(self, features):
        prediction = self.model.predict([features])
        return prediction[0]