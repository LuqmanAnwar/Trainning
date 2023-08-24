import numpy as np
import pandas as pd
import streamlit as st
import pickle


st.title('Bank Loan')
st.text('Loan Approval')

gender = st.radio("Gender", ["Female", "Male"])

married = st.radio("Are you married?", ["No", "Yes"])

dependents = st.slider("Dependents", 0, 10)

education = st.radio("Education",["Graduate", "Not Graduate"])

selfEmp = st.radio("Self Employed?", ["No", "Yes"])

appIncome = st.text_input("Applicant Income")
coIncome = st.text_input("Co-Applicant Income")
LoanAmt = st.text_input("Loan Amount")
term = st.slider("Terms",0,360)
CreditHistory = 1
area = st.selectbox("Select Area",["Semi-Urban","Urban"])


click = st.button("Submit")

if click:
    
    if area == 'Urban':
        area = 0
    else:
        area = 1
    
    
    if gender=="Female":
        gender = 0
    else: 
        gender = 1
        
    if married=="No":
        married = 0
    else:
        married = 1
    
    if education =="Graduate":
        education = 0
    else:
        education = 1
    
    if selfEmp == "No":
        selfEmp = 0
    else:
        selfEmp = 1
        
    if area == "Semi-Urban":
        area = 0
    else:
        area = 1
        
        
    dat = [[gender, married, dependents, education, selfEmp, appIncome, coIncome, LoanAmt, term, CreditHistory, area]]

    model = pickle.load(open('svm_model.pkl','rb'))
    res = model.predict(dat)

    if res==1:
        
        st.text("Your application will most likely to be approved! :)")
    else:
        st.text("Your application will most probably be rejected! :(")
        
