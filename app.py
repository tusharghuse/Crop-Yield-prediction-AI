from flask import Flask, request, jsonify, render_template
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from utils.preprocessor import load_and_preprocess

app = Flask(__name__)

# Train model once
X, y = load_and_preprocess("data/dataset.csv")
model = RandomForestRegressor()
model.fit(X, y)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([[ 
        data['rainfall'],
        data['temperature'],
        data['humidity'],
        data['soil_type']
    ]])

    prediction = model.predict(features)[0]

    return jsonify({"predicted_yield": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)