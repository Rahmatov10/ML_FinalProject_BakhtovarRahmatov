import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
st.title('Final Project ML Course. Bakhtovar Rahmatov. Loan approval classifier')

st.write('Hello world!')
# Загрузка данных

df = pd.read_csv('Loan - Loan.csv')

with st.sidebar:
  st.header("Введите признаки: ")
