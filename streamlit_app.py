st.title('Final Project ML Course. Bakhtovar Rahmatov. Loan approval classifier')

st.write('Hello world!')
# Загрузка данных
with st.expander('Исходные данные'):
    df = pd.read_csv('Loan-Loan.csv')
