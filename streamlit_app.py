import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
st.title('Final Project ML Course. Bakhtovar Rahmatov. Loan approval classifier')

st.write('Hello world!')

df = pd.read_csv("https://raw.githubusercontent.com/Rahmatov10/ML_FinalProject_BakhtovarRahmatov/refs/heads/master/insurance%20-%20insurance.csv")
print(df.head())
