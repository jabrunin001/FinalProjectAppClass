import joblib
import numpy as np

# Load the trained model
model = joblib.load('traffic_model.pkl')

# Example input data (e.g., POSTED_SPEED_LIMIT, WEATHER_CONDITION, LIGHTING_CONDITION, FIRST_CRASH_TYPE)
# Note: The values must be encoded in the same way as during training
input_data = np.array([[30, 2, 1, 3]])  # Example encoded features

# Predict the outcome using the trained model
prediction = model.predict(input_data)
print("Predicted injury count:", prediction[0])
