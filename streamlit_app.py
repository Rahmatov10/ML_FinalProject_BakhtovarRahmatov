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
