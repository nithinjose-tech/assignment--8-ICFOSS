import streamlit as st
import pandas as pd
import pickle
st.write("""
# Admission Predictor using SVR 
 """)
svr_regressor = open('svr_model.pkl','rb')
regressor = pickle.load(svr_regressor)
#Text Input
gre_score = st.text_input("Enter the GRE Score",)
toefl_score = st.text_input("Enter the TOEFL Score")
university_rating = st.text_input("Enter the University Rating")
sop = st.text_input("Enter the SOP Score")
lor = st.text_input("Enter the LOR Score")
cGPA = st.text_input("Enter the CGPA Score")
Research = st.text_input("Enter the Research Score")
submit = st.button("Predict")

if submit:
	result = regressor.predict([[gre_score,toefl_score,university_rating,sop,lor,cGPA,Research]])
	st.write("The possiblity of getting admission is:",result[0])
	
	