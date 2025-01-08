import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
st.title('Final Project ML Course. Bakhtovar Rahmatov. Loan approval classifier')

st.write('Hello world!')
# Загрузка данных

df = pd.read_csv('Loan - Loan.csv')
 print(df.head())

with st.sidebar:
  st.header("Введите признаки: ")
  st.header("Введите признаки: ")
  island = st.selectbox('Island', ('Torgersen', 'Dream', 'Biscoe'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 44.5)
  bill_depth_mm = st.slider('Bill length (mm)', 13.1, 21.5, 17.3)
  flipper_length_mm = st.slider('Flipper length (mm)', 32.1, 59.6, 44.5)
  body_mass_g = st.slider('Body mass (g)', 32.1, 59.6, 44.5)
  gender = st.selectbox('Gender', ('female', 'male'))
