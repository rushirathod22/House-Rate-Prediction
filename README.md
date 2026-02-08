# House Price Prediction – Machine Learning Web Application

An end-to-end Machine Learning application that predicts house prices using property features and serves predictions through a modern web interface.

The project demonstrates the complete workflow from data preprocessing and model training to backend integration and user-facing deployment.

---

## Overview

This application uses a supervised regression model trained on real housing data to estimate property prices.  
A Flask backend exposes the trained model, while a responsive HTML/CSS frontend allows users to interact with the system in real time.

---

## Features

- Data preprocessing and feature engineering  
- Regression-based price prediction  
- Flask backend for model serving  
- Modern, responsive frontend UI  
- End-to-end integration (UI → Backend → ML Model)  
- Clean, deployment-ready project structure  

---

## Technology Stack

### Machine Learning
- Python  
- Pandas  
- NumPy  
- Scikit-learn  

### Backend
- Flask  

### Frontend
- HTML  
- CSS  

---

## Dataset

- **Source:** Kaggle Housing Price Dataset  
- **Target Variable:** House Price  
- **Input Features:**  
  - Area  
  - Bedrooms  
  - Bathrooms  
  - Stories  
  - Parking  
  - Furnishing Status  
  - Amenities (Air Conditioning, Basement, Preferred Area, etc.)

---

## Model Details

- **Algorithm:** Linear Regression  
- **Evaluation Metric:** R² Score  
- **Performance:** R² ≈ 0.65  

The model was selected based on its interpretability, stability, and performance on unseen data.

---

## Application Screenshots

### User Interface
<img width="1889" height="967" alt="image" src="https://github.com/user-attachments/assets/4d385430-48e9-45b0-873f-00d755f853f4" />


### Prediction Output
<p align="center">
  <img src="screenshots/ui_result.png" width="800">
</p>

---

## Project Structure

House-Price-Prediction-ML/
├── app.py
├── house_price_model.pkl
├── features.pkl
├── Housing.csv
├── housing_price.ipynb
├── requirements.txt
├── README.md
├── templates/
│ └── index.html




### Install Dependencies
pip install -r requirements.txt

### Run the Application
  python app.py

4. Access the Application

### Open your browser and navigate to:

http://127.0.0.1:5000

### Key Learnings

### Importance of feature selection and data preprocessing

Model evaluation and validation techniques

Integrating machine learning models with web applications

Designing user-friendly interfaces for ML systems

Structuring ML projects for deployment and collaboration

### Author

### Rushikesh Rathod
B.Tech Computer Science (AI)
Interested in Machine Learning and Full-Stack Development

### Future Enhancements

Implement advanced regression models (Random Forest, Gradient Boosting)

Deploy application to cloud platforms (Render / Railway)

Expose predictions via REST API

Add confidence intervals for predictions
