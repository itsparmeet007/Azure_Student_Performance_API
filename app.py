from flask import Flask, request, jsonify, render_template
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
    return render_template("index.html")

@app.route("/predict-form", methods=["POST"])
def predict_form():
    try:
        data = request.form

        input_data = [
            int(data.get("sex", 1)),
            int(data.get("age")),
            int(data.get("parent_status", 1)),
            int(data.get("mother_education", 3)),
            int(data.get("father_education", 3)),
            int(data.get("travel_time")),
            int(data.get("study_time")),
            int(data.get("class_failures", 0)),
            int(data.get("school_support", 1)),
            int(data.get("family_support", 1)),
            int(data.get("extra_paid_classes", 0)),
            int(data.get("higher_ed", 1)),
            int(data.get("internet_access", 1)),
            int(data.get("romantic_relationship", 0)),
            int(data.get("family_relationship", 4)),
            int(data.get("free_time", 3)),
            int(data.get("social", 3)),
            int(data.get("weekday_alcohol", 1)),
            int(data.get("weekend_alcohol", 2)),
            int(data.get("health", 3)),
            int(data.get("absences")),
            int(data.get("grade_1")),
            int(data.get("grade_2")),
            int(data.get("family_size_Less than or equal to 3", 1)),
            int(data.get("school_choice_reason_home", 0)),
            int(data.get("school_choice_reason_other", 0)),
            int(data.get("school_choice_reason_reputation", 1))
        ]

        prediction = model.predict([input_data])

        return render_template("index.html", prediction=round(prediction[0], 2))

    except Exception as e:
        return str(e)
if __name__ == "__main__":
    app.run(debug=True)