import streamlit as st
import pickle
import numpy as np

model = pickle.load(open(r"educateprocess.pkl", 'rb'))

st.title('Epm pass-fail predictor')

cols = []

total_marks = st.number_input("Enter total marks", value=0.0, step=0.1)

for i in range(16):
    col = st.number_input(f"Enter lab marks {i+1}", value=0.0, step=0.1)
    cols.append(col)

cols.append(total_marks)

if st.button('Predict pass/fail'):
    if total_marks:
        marks = np.array([cols[-1]]).reshape(1, -1)
        prediction = model.predict(marks)

        if prediction == 0:
            st.write('Result: Good & pass')
        elif prediction == 1:
            st.write('Result: fair & pass')
        else:
            st.write('Result: weak & fail')
    else:
        st.error("Please fill in the total marks field.")

# Embedding YouTube video
video_url = "https://youtu.be/aWxQc4mCy_w"  # Replace with your YouTube video URL or ID
st.video(video_url)
