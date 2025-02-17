import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
st.title('Final Project ML Course. Bakhtovar Rahmatov. Loan approval classifier')


# 1) Project
st.subheader("Loan classier")
st.write("""
**Data source**: Kaggle.

Why did i select this topic:
#### For the final project, I chose to build a classifier model for new loan requests. I chose this topic because back in 2015, 
one of my co-workers built a "lead-scoring" model, which gives "grades" to potential new customers, and first phone calls would be 
made based on the calculated "grade". This model showed significant improvement of lead conversion and sales. I was always curious how 
he used historical data to create this model on a simple Excel spreadsheet. Thanks to this course, I learned about ML and the power it gives to get insights 
from the data. Now, bismillah ... 

""")

st.subheader("1. EDA")
st.write("""

- Analyses of numerical columns. 
- Deleting outliers.
- Recreating DataFrame and visual display of numerical factors distribution

""")

st.subheader("2. Preprocessing")
st.write("""

- Correlation matrix and heatmap for numerical factors.
- Target Mean Encoding
- recreating correlation matrix for all the factors and target output

""")

st.subheader("3. Models")
st.write("""

- Logistics Regression
- Random Forest
- Catboost
- KNN

""")

st.subheader("4. Colclusion")
st.write("""

All the four mentioned models and detailed analysis were completed on Jupyter notebook.
Model with the best accuracy resultL 93% Random Forest is used in this model

""")

st.markdown("---")





  
df = pd.read_csv("loan_data.csv")


with st.expander('Data'):
  st.write("X")
  X_raw = df.drop(['loan_status', 'loan_percent_income'], axis=1)
  st.dataframe(X_raw)

  st.write("y")
  y_raw = df.loan_status
  st.dataframe(y_raw)

with st.sidebar:
  st.header("Введите признаки: ")
  person_age = st.slider("age (y)", 18, 1, 150)
  person_gender = st.selectbox('Gender', ('male', 'female'))
  person_income = st.slider("income (USD/year)", 0, 1000, 1000000)
  person_education = st.selectbox("Educaiton level", ('Associate', 'Bachelor', 'Doctorate', 'High School', 'Master'))
  person_emp_exp = st.slider("Experience (years)", 0, 1, 100)
  person_home_ownership = st.selectbox("Home ownership", ('MORTGAGE', 'OTHER', 'OWN', 'RENT'))
  loan_amnt = st.slider("Loan amount (USD)", 0, 1, 100000)
  loan_intent = st.selectbox("Loan intent", ('DEBTCONSOLIDATION', 'EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE'))
  loan_int_rate = st.slider("Loan interest rate (%)", 1, 1, 30) 
 
  cb_person_cred_hist_length = st.slider("Credit history length (y) ", 0, 1, 40)
  credit_score = st.slider("Credit score (points) ", 100, 10, 1000)
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
            'cb_person_cred_hist_length': cb_person_cred_hist_length,
            'credit_score':credit_score,
            'previous_loan_defaults_on_file': previous_loan_defaults_on_file}  # Добавлен пол
    input_df = pd.DataFrame(data, index=[0])

  # Объединяем с исходными данными для корректного кодирования
    input_data = pd.concat([input_df, X_raw], axis=0)

# Кодирование категориальных переменных
encode = ['person_gender', 'person_education', 'person_home_ownership', 'loan_intent', 'previous_loan_defaults_on_file']
input_data_encoded = pd.get_dummies(input_data, columns=encode)

# Отделяем строку с вводом пользователя
X_input = input_data_encoded[:1]

# Обработка категориальных переменных для основного набора данных
df_encoded = pd.get_dummies(X_raw, columns=encode)

# Разделение данных на обучающую и тестовую выборки
X = df_encoded
y = y_raw
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели RandomForestClassifier с корректным параметром max_features
rf_clf = RandomForestClassifier(n_estimators=200, random_state=42)
rf_clf.fit(X_train, y_train)

# Прогнозирование и оценка модели
y_pred_clf = rf_clf.predict(X_test)

# Прогнозирование
prediction = rf_clf.predict(X_input)
prediction_proba = rf_clf.predict_proba(X_input)

# Отображение результата
st.subheader('Probability of Loan approval')
df_prediction_proba = pd.DataFrame(prediction_proba, columns=['Rejected', 'approved'])
st.dataframe(df_prediction_proba)

# Вывод результата
if prediction[0] == 1:
    st.success("Loan approved")
else:
    st.success("Loan rejected")
  
