#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 13:15:03 2025

@author: satyamgajjar
"""

import pickle
import streamlit as st 
from streamlit_option_menu import option_menu


#loading the saved models
diabetes_model = pickle.load(open("/Users/satyamgajjar/Library/Mobile Documents/com~apple~CloudDocs/Satyam's Mac/Learnings/Data Science/Code With Harry - Data Science/14 Practicing ML using Scikit-learn/20 Projects/22 Deploy ML Project Streamlit - Multiple Disease Prediction System/diabetes_model.sav", "rb"))

heartdisease_model = pickle.load(open("/Users/satyamgajjar/Library/Mobile Documents/com~apple~CloudDocs/Satyam's Mac/Learnings/Data Science/Code With Harry - Data Science/14 Practicing ML using Scikit-learn/20 Projects/22 Deploy ML Project Streamlit - Multiple Disease Prediction System/heartdisease_model.sav", "rb"))

parkinsons_model = pickle.load(open("/Users/satyamgajjar/Library/Mobile Documents/com~apple~CloudDocs/Satyam's Mac/Learnings/Data Science/Code With Harry - Data Science/14 Practicing ML using Scikit-learn/20 Projects/22 Deploy ML Project Streamlit - Multiple Disease Prediction System/parkinson_model.sav", "rb"))

                                    
#sidebar for navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Predicition System using ML", 
                           ['Diabetes Prediction',
                            'Heart Disease Predicition',
                            "Parkinsons Prediction"],
                           icons = ['activity','heart','person'],
                           default_index=0)
    
    
#Diabetes Prediction Stage------------------------------------------------------------------------------------------------------------------
if (selected == 'Diabetes Prediction'):
    
    #pg title
    st.title('Diabetes Prediction by satyam')
    
    #Getting the input data 
    #columns for input field
    col1, col2, col3 = st.columns(3)
    
    with col1:
        #take user input
        Pregnancies = st.text_input("No. of Pregnancies")
        
    with col2:
        Glucose = st.text_input("Glucose Value")
        
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
        
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")

    with col2:
        Insulin = st.text_input("Insulin Value")
        
    with col3:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction Value")

    with col2:
        Age = st.text_input("Age of Person")
    
    
    
    #Code for Prediction
    diab_diagnosis = ''
    
    #Creating a button for Prediction, pass the values in list
    if st.button('Diabetes Test Result'):
        diab_predictions = diabetes_model.predict([[Pregnancies,	Glucose, BloodPressure,	SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if (diab_predictions[0]==1):
            diab_diagnosis = "The person is Diabetic"
        else:
            diab_diagnosis = "The person is not diabetic"
            
    st.success(diab_diagnosis)
    
    
    
# Heart Disease Stage----------------------------------------------------------------------------------------------------------------------
if (selected == 'Heart Disease Predicition'):
    
    st.title("Heart Disease Prediction by satyam")
    
    # Getting user input
    col1, col2, col3 = st.columns(3)
 
    with col1:
        age = st.text_input("Age")
        
    with col2:
        sex = st.text_input("Sex Value")
        
    with col3:
        cp = st.text_input("Chest Pain Type (cp)")
        
    with col1:
        trestbps = st.text_input("Resting Blood Pressure (trestbps)")

    with col2:
        chol = st.text_input("Cholesterol (chol)")
        
    with col3:
        fbs = st.text_input("Fasting Blood Sugar (fbs)")

    with col1:
        restecg = st.text_input("Resting ECG (restecg)")

    with col2:
        thalach = st.text_input("Max Heart Rate (thalach)")
        
    with col3:
        exang = st.text_input("Exercise Induced Angina (exang)")
    
    with col1:
        oldpeak = st.text_input("Oldpeak")

    with col2:
        slope = st.text_input("Slope")
        
    with col3:
        ca = st.text_input("ca Value")
        
    with col1:
        thal = st.text_input("thal Value")
    
    
    # Result display variable
    heart_diagnosis = ""
    
    # Prediction logic
    if st.button('Heart Test Result'):
        try:
            # Convert all inputs to float
            user_input = [
                float(age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang),
                float(oldpeak), float(slope), float(ca), float(thal)
            ]

            heart_predictions = heartdisease_model.predict([user_input])
    
            if heart_predictions[0] == 1:
                heart_diagnosis = "The person HAS a Heart Problem"
            else:
                heart_diagnosis = "The person does NOT have a Heart Problem"
        
        except ValueError:
            heart_diagnosis = "Please enter all values correctly in numeric form."
            
    st.success(heart_diagnosis)

    
    
##Parkinsons Prediction Stage------------------------------------------------------------------------------------------------------------------
## 0 - healthy people, 1 - they have parkinsons disease
if (selected == 'Parkinsons Prediction'):
    
    #pg title
    st.title("Parkinsons Prediction by satyam")
    

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        MDVP_Fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        MDVP_Flo = st.text_input("MDVP:Flo(Hz)")

    with col1:
        MDVP_Jitter_percent = st.text_input("MDVP:Jitter(%)")
    with col2:
        MDVP_Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col3:
        MDVP_RAP = st.text_input("MDVP:RAP")

    with col1:
        MDVP_PPQ = st.text_input("MDVP:PPQ")
    with col2:
        Jitter_DDP = st.text_input("Jitter:DDP")
    with col3:
        MDVP_Shimmer = st.text_input("MDVP:Shimmer")

    with col1:
        MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col2:
        Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
    with col3:
        Shimmer_APQ5 = st.text_input("Shimmer:APQ5")

    with col1:
        MDVP_APQ = st.text_input("MDVP:APQ")
    with col2:
        Shimmer_DDA = st.text_input("Shimmer:DDA")
    with col3:
        NHR = st.text_input("NHR")

    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")

    with col1:
        spread1 = st.text_input("spread1")
    with col2:
        spread2 = st.text_input("spread2")
    with col3:
        D2 = st.text_input("D2")

    with col1:
        PPE = st.text_input("PPE")

    # Prediction output variable
    parkinson_diagnosis = ""

    # Predict button
    if st.button("Parkinsons Test Result"):
        try:
            # Convert all inputs to float
            user_input = [
                float(MDVP_Fo), float(MDVP_Fhi), float(MDVP_Flo),
                float(MDVP_Jitter_percent), float(MDVP_Jitter_Abs),
                float(MDVP_RAP), float(MDVP_PPQ), float(Jitter_DDP),
                float(MDVP_Shimmer), float(MDVP_Shimmer_dB),
                float(Shimmer_APQ3), float(Shimmer_APQ5), float(MDVP_APQ),
                float(Shimmer_DDA), float(NHR), float(HNR),
                float(RPDE), float(DFA), float(spread1), float(spread2),
                float(D2), float(PPE)
            ]

            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinson_diagnosis = "The person HAS Parkinsons Disease"
            else:
                parkinson_diagnosis = "The person does NOT have Parkinsons Disease"

        except ValueError:
            parkinson_diagnosis = "Please enter all values correctly in numeric form."

    st.success(parkinson_diagnosis)

    
    
    
    
    
    
    
    
    
    
    