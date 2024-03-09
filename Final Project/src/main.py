from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import joblib
import numpy as np

app = Flask(__name__)
api = Api(app)

class Predict(Resource):
    def post(self):
        data = request.get_json()

        # Load the trained model
        model = joblib.load('traffic_model.pkl')

        # Extract features from the request
        features = np.array([[
            data['posted_speed_limit'],
            data['weather_condition'],
            data['lighting_condition'],
            data['first_crash_type']
        ]])

        # Make prediction
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})

api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True)
