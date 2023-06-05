import streamlit as st
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open(r"C:\Users\mraja\Downloads\ml project\educte.pkl", 'rb'))

st.title('Epm pass-fail predictor')

cols = []
marks = []

features_to_drop = ['student id', 'total point', 'es3.1']

for i in range(17):
    if i+1 in features_to_drop:
        continue
    col = st.number_input(f"Enter lab marks {i+1}")
    cols.append(col)

if st.button('Predict pass/fail'):
    marks = np.array(cols).reshape(1, -1)
    prediction = model.predict(marks)

    if prediction == 0:
        st.write('Result: Good & pass')
    elif prediction == 1:
        st.write('Result: fair & pass')
    else:
        st.write('Result: weak & fail')
