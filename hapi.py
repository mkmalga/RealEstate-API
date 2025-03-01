from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model and feature order
model = joblib.load('hyderabad_realestatemodel.pkl')
feature_order = pd.read_csv("feature_order.csv", header=None)[0].tolist()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print("Received Data:", data) 

    # Validate that all required features are present
    missing = [feat for feat in feature_order if feat not in data]
    if missing:
        return jsonify({"error": f"Missing features: {missing}"}), 400

    # Prepare input as 2D array
    #input_features = [data[feat] for feat in feature_order]
    #input_array = np.array(input_features).reshape(1, -1)
    input_df = pd.DataFrame([data])
    # Predict house price
    prediction = model.predict(input_df)
    print("Prediction:", prediction[0])  # Debugging
    return jsonify({'predicted_price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
