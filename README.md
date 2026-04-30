# 🎓 Student Performance Prediction System

![Live API](https://img.shields.io/badge/API-Live-green)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![Azure](https://img.shields.io/badge/Cloud-Azure-blue)
![Deployment](https://img.shields.io/badge/Deployed%20on-Azure-success)

---

## 👨‍💻 Author

**Parmeet Singh**

---

## 🚀 Live Application

👉 https://performanceapi-cjdzfkeygxcpb0dh.eastasia-01.azurewebsites.net

---

## 📌 Overview

A **full-stack Machine Learning web application** that predicts a student’s final grade using a trained Random Forest model.

✔ REST API (Flask)
✔ Web Interface (HTML Form)
✔ Cloud Deployment (Azure)
✔ CI/CD Pipeline (GitHub Actions)

---

## ✨ Features

* Predict student performance using ML
* Web-based UI for easy interaction
* REST API support
* Real-time prediction
* Cloud deployment (Azure App Service)
* Automated CI/CD using GitHub Actions

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* NumPy & Pandas
* Joblib
* Gunicorn
* HTML (Frontend UI)
* Azure App Service
* GitHub Actions

---

## 📂 Project Structure

```
├── app.py                # Flask Application
├── model.pkl             # Trained ML model
├── features.json         # Feature order
├── requirements.txt      # Dependencies
├── templates/
│   └── index.html        # Frontend UI
└── .github/workflows     # CI/CD pipeline
```

---

## 🔗 Endpoints

### ✅ GET /

Loads the web interface (HTML UI)

---

### ✅ POST /predict

Returns prediction in JSON format (API)

---

### ✅ POST /predict-form

Handles form submission and displays prediction on the webpage

---

## 🧪 Example API Request

```json
{
  "feature1": 10,
  "feature2": 20,
  "feature3": 30
}
```

---

## 📤 Example API Response

```json
{
  "predicted_final_grade": 11.585
}
```

---

## 🖥️ Web Interface

Users can:

* Enter input values
* Submit form
* Get prediction instantly

Example Output:

```
Predicted Final Grade: 19.28
```

---

## ⚙️ How It Works

1. User inputs data via form or API
2. Flask receives the request
3. Data is arranged using `features.json`
4. Model (`model.pkl`) predicts output
5. Result is returned (JSON or UI)

---

## 🔄 CI/CD Pipeline

```
GitHub → GitHub Actions → Azure App Service → Live Deployment
```

* Push code → auto deploy
* No manual deployment required

---

## 🧪 Testing

You can test using:

* Thunder Client (VS Code)
* Postman
* Browser (for UI)

---

## 📈 Future Improvements

* Improve UI using Bootstrap
* Add input validation
* Add authentication
* Add Swagger documentation
* Add charts/visualization
* Improve model accuracy

---

## 👨‍💻 About Me

**Parmeet Singh**
Aspiring ML Engineer / Data Scientist

* Skilled in Python, Machine Learning, and Web Development
* Interested in AI, Cloud, and Backend Development

---

## 📬 Contact

GitHub: https://github.com/itsparmeet007

---

## ⭐ Project Highlights

✔ End-to-end ML deployment
✔ Full-stack (UI + API)
✔ Cloud-hosted application
✔ CI/CD enabled
✔ Real-time prediction system

---

## 📄 License

This project is for educational purposes.


## 📬 Contact

* GitHub: https://github.com/itsparmeet007

---

## ⭐ Acknowledgement

This project demonstrates end-to-end ML deployment:
from training → API → cloud deployment 🚀
