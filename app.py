from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# Load the pickled model
with open('california_model.pkl', 'rb') as file:
    regmodel = pickle.load(file)

# Load the scaler
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Home route


@app.route('/')
def home():
    return render_template('index.html')

# Prediction route (API)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Example input: {"features": [8.3252, 41, 6.984126984, 1.023809524, 322, 2.555555556, 37.88, -122.23]}
        features = np.array(data['features']).reshape(1, -1)

        # ✅ Scale the input features
        scaled_features = scaler.transform(features)

        # ✅ Predict using the scaled data
        prediction = regmodel.predict(scaled_features)

        return jsonify({
            "prediction": float(prediction[0])
        })

    except Exception as e:
        return jsonify({"error": str(e)})


# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)  # Keep 5000 inside container
