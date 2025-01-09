import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
st.title('Final Project ML Course. Bakhtovar Rahmatov. Loan approval classifier')

st.write('Hello world!')

df = pd.read_csv("loan_data.csv")


with st.expander('Data'):
  st.write("X")
  X_raw = df.drop('loan_status', axis=1)
  st.dataframe(X_raw)

  st.write("y")
  y_raw = df.loan_status
  st.dataframe(y_raw)

with st.sidebar:
  st.header("Введите признаки: ")
  person_age = st.slider("age (y)", 18, 50, 99)
  person_gender = st.selectbox('Gender', ('Male', 'Female'))
  person_income = st.slider("income (USD/year)", 0, 200000, 40000)
  person_education = st.selectbox("Educaiton level", ('Associate', 'Bachelor', 'Doctorate', 'High School', 'Master'))
  person_emp_exp = st.slider("Experience (years)", 0, 50, 100)
  person_home_ownership = st.selectbox("Home ownership", ('MORTGAGE', 'OTHER', 'OWN', 'RENT'))
  loan_amnt = st.slider("Loan amount (USD)", 0, 50000, 100000)
  loan_intent = st.selectbox("Loan intent", ('DEBTCONSOLIDATION', 'EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE'))
  loan_int_rate = st.slider("Loan interest rate (%)", 1, 15, 30) 
  loan_pencent_income = st.slider("Loan amount / Income ", 0, 1) 
  cb_person_cred_hist_length = st.slider("Credit history length (y) ", 0, 20, 40)
  credit_score = st.slider("Credit score (points) ", 100, 1000)
  previous_loan_defaults_on_file = st.selectbox('Defaults', ('Yes', 'No'))

# Визуализация данных
with st.expander('Визуализация данных'):
    st.bar_chart(data=df['person_gender'].value_counts())
    st.bar_chart(data=df['loan_intent'].value_counts())

# Собираем вводные данные в DataFrame
    data = {'person_age': person_age,
            'person_gender': person_gender,
            'person_income': person_income,
            'person_education': person_education,
            'person_emp_exp': person_emp_exp,
            'person_home_ownership': person_home_ownership,
            'loan_amnt': loan_amnt,
            'loan_intent': loan_intent,
            'loan_int_rate': loan_int_rate,
            'loan_pencent_income': loan_pencent_income,
            'cb_person_cred_hist_length': cb_person_cred_hist_length,
            'credit_score':credit_score,
            'previous_loan_defaults_on_file': previous_loan_defaults_on_file}  # Добавлен пол
    input_df = pd.DataFrame(data, index=[0])

  # Объединяем с исходными данными для корректного кодирования
    input_data = pd.concat([input_df, X_raw], axis=0)
  
