import streamlit as st
import pickle
import numpy as np

model = pickle.load(open(r"C:\Users\mraja\Downloads\ml project\edupm.pkl", 'rb'))

st.title('Epm pass-fail predictor')

cols = []

features_to_drop = ['student id', 'total marks']

for i in range(16):
    if i+1 in features_to_drop:
        continue
    col = st.number_input(f"Enter lab marks {i+1}", value=0.0, step=0.1)
    cols.append(col)

total_marks = st.number_input("Enter total marks", value=0.0, step=0.1)

cols.append(total_marks)

if st.button('Predict pass/fail'):
    marks = np.array(cols).reshape(1, -1)

    if all(cols):
        prediction = model.predict(marks)
        if prediction == 0:
            st.write('Result: Good & pass')
        elif prediction == 1:
            st.write('Result: fair & pass')
        else:
            st.write('Result: weak & fail')
    else:
        st.error("Please fill in all the required fields.")
