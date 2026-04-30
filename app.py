from flask import Flask, request, jsonify
import joblib
import json

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

# load feature order
with open('features.json','r') as f:
    feature_names = json.load(f)

@app.route("/")
def home():
    return "Student Performance API Running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json # expecting dictionary
        
        # Convert input dict -> ordered list
        input_data = [data[feature] for feature in feature_names]
        prediction = model.predict([input_data])
        
        return jsonify({
            "predicted_final_grade": float(prediction[0])
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)