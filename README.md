# 🎓 Student Performance Prediction API

![Live API](https://img.shields.io/badge/API-Live-green)


**Author:** Parmeet Singh

A machine learning REST API that predicts a student’s final grade using a trained Random Forest model.
The API is fully deployed on Azure and accessible over the internet.

---

## 🚀 Live API

```
https://performanceapi-cjdzfkeygxcpb0dh.eastasia-01.azurewebsites.net
```

---

## 📌 Features

* Predict student performance using ML
* REST API built with Flask
* Deployed on cloud (Azure App Service)
* CI/CD pipeline using GitHub Actions
* Fast and scalable inference

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* NumPy & Pandas
* Joblib
* Gunicorn
* Azure App Service
* GitHub Actions

---

## 📂 Project Structure

```
├── app.py                # Flask API
├── model.pkl             # Trained ML model
├── features.json         # Feature order
├── requirements.txt      # Dependencies
└── .github/workflows     # CI/CD pipeline
```

---

## 🔗 API Endpoints

### ✅ GET /

Check if API is running

**Response:**

```
API is running
```

---

### ✅ POST /predict

Predict student final grade

**URL:**

```
/predict
```

**Method:** POST

**Headers:**

```
Content-Type: application/json
```

---

## 📥 Example Request

```json
{
  "feature1": 10,
  "feature2": 20,
  "feature3": 30
}
```

---

## 📤 Example Response

```json
{
  "predicted_final_grade": 11.585
}
```

---

## ⚙️ How It Works

1. Input features are received via API
2. Data is arranged based on `features.json`
3. Model (`model.pkl`) processes input
4. Prediction is returned as JSON

---

## 🔄 CI/CD Pipeline

* Code pushed to GitHub
* GitHub Actions automatically builds & deploys
* Azure App Service hosts the API

---

## 🧪 Testing

You can test the API using:

* Thunder Client (VS Code)
* Postman
* cURL

---

## 📈 Future Improvements

* Add input validation
* Add Swagger API documentation
* Build frontend UI
* Add logging & monitoring
* Improve model accuracy

---

## 👨‍💻 About Me

**Parmeet Singh**
Aspiring ML Engineer / Data Scientist

* Skilled in Python, Machine Learning, and Web APIs
* Interested in AI, Cloud, and Backend Development

---

## 📬 Contact

* GitHub: https://github.com/itsparmeet007

---

## ⭐ Acknowledgement

This project demonstrates end-to-end ML deployment:
from training → API → cloud deployment 🚀
