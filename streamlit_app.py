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

# Визуализация данных
# List of numerical columns to plot
numerical_columns = ['person_age', 'person_income', 'person_emp_exp', 'loan_amnt', 
                     'loan_int_rate', 'loan_percent_income', 'cb_person_cred_hist_length', 
                     'credit_score']

# Create a figure with subplots
fig, axs = plt.subplots(3, 3, figsize=(15, 15))  # Adjust the number of rows and columns as needed
axs = axs.flatten()  # Flatten the axes for easy iteration

# Plot histograms for each numerical column
for i, col in enumerate(numerical_columns):
    sns.histplot(data[col], kde=True, ax=axs[i], bins=30)  # You can adjust the number of bins
    axs[i].set_title(f"Distribution of {col}")
    axs[i].set_xlabel(col)
    axs[i].set_ylabel("Frequency")

# Tight layout to avoid overlapping labels
plt.tight_layout()
plt.show()
