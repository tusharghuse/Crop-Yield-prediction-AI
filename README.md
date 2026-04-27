# 🌾 Crop Yield Prediction using Machine Learning

## 📌 Project Overview

This project focuses on predicting crop yield using Machine Learning techniques and Data Analytics.
It uses environmental and agricultural factors such as rainfall, temperature, humidity, and soil type to estimate crop production.

---

## 🎯 Objectives

* Build a machine learning model for crop yield prediction
* Compare multiple algorithms
* Improve prediction accuracy
* Assist farmers and policymakers in decision-making

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Flask

---

## 📂 Project Structure

```
crop-yield-prediction/
│
├── data/
│   └── dataset.csv
│
├── models/
│   └── train_model.py
│
├── utils/
│   ├── preprocess.py
│   └── evaluate.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### Step 1: Clone the repository

```
git clone <your-repo-link>
cd crop-yield-prediction
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Run Model Training

```
python models/train_model.py
```

### Run Flask App

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🔮 API Usage

### Endpoint:

```
POST /predict
```

### Sample Input:

```json
{
  "rainfall": 120,
  "temperature": 30,
  "humidity": 70,
  "soil_type": 1
}
```

### Output:

```json
{
  "predicted_yield": 26.5
}
```

---

## 📊 Machine Learning Models Used

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

---

## 📈 Evaluation Metrics

* RMSE (Root Mean Squared Error)
* MAE (Mean Absolute Error)
* R² Score

---

## 🚀 Future Scope

* Real-time data integration
* Mobile application for farmers
* Integration with satellite data

---

## 👨‍💻 Authors

* Tushar Sunil Ghuse


## 📄 License

This project is for academic and research purposes.
