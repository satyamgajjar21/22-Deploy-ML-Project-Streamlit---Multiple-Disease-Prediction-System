# Multiple Disease Prediction System Using Machine Learning

## Overview
This project is a machine learning powered web application built using Streamlit.  
It allows users to predict the likelihood of three medical conditions using trained machine learning models.

The application provides an interactive user interface where medical parameters can be entered and predictions are generated instantly.

## Diseases Covered
1 Diabetes Prediction  
2 Heart Disease Prediction  
3 Parkinsons Disease Prediction  

Each disease uses a separate trained machine learning model.

## Technologies Used
Python  
Streamlit  
Scikit Learn  
NumPy  
Pickle  
Streamlit Option Menu  

## Application Features
Sidebar based navigation for switching between disease modules  
Separate input forms for each disease  
Real time prediction results  
User friendly multi column layout  
Model loading using pickle files  

## Project Structure
multiple disease predict.py  
diabetes_model.sav  
heartdisease_model.sav  
parkinson_model.sav  

## Diabetes Prediction Module
Takes the following inputs  
Pregnancies  
Glucose  
Blood Pressure  
Skin Thickness  
Insulin  
BMI  
Diabetes Pedigree Function  
Age  

The model predicts whether the person is diabetic or not.

## Heart Disease Prediction Module
Takes the following inputs  
Age  
Sex  
Chest Pain Type  
Resting Blood Pressure  
Cholesterol  
Fasting Blood Sugar  
Resting ECG  
Maximum Heart Rate  
Exercise Induced Angina  
Oldpeak  
Slope  
CA  
Thal  

The model predicts the presence or absence of heart disease.

## Parkinsons Prediction Module
Uses voice measurement based medical parameters such as  
MDVP frequencies  
Jitter values  
Shimmer values  
NHR and HNR  
RPDE  
DFA  
Spread values  
PPE  

The model predicts whether the person has Parkinsons disease.

## How to Run the Project
Install required dependencies

pip install streamlit scikit-learn numpy streamlit-option-menu

Run the application

streamlit run multiple disease predict.py

## Notes
Ensure all model files are present in the correct path  
Input values must be numeric  
The app uses local pickle files for prediction  

## Author
Satyam Gajjar
