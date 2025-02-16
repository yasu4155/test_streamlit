import streamlit as st
import numpy as np
import time
from PIL import Image

st.title('Streamlit入門')
st.write('progress bar')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration: {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

left_column, right_column = st.columns(2)
button = left_column.button('push')
if button:
    right_column.write('here is right column')

expandar1 = st.expander('question 1')
expandar1.write('answer 1')
expandar2 = st.expander('question 2')
expandar2.write('answer 2')
expandar3 = st.expander('question 3')
expandar3.write('answer 3')
expandar4 = st.expander('question 4')
expandar4.write('answer 4')
expandar5 = st.expander('question 5')
expandar5.write('answer 5')

option = st.selectbox(
    'select your favorite number',
    list(range(1, 11))
)
'your favorite number is', option, '.'

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='background', use_container_width =True)

text = st.text_input('enter your hobby')
condition = st.slider('condition', 0, 100, 50,)

'Your hobby: ', text
'Condition: ', condition