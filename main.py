import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image

st.title('Streamlit入門')
st.write('Interactive Wedgets')

df = pd.DataFrame({
    '1st row': [1, 2, 3, 4, 5],
    '2nd row': [10, 20, 30, 40, 50]
})

if st.checkbox('Table'):
    st.write(df)

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

if st.checkbox('Graph'):
    st.line_chart(df)
    st.area_chart(df)
    st.bar_chart(df)
    
df = pd.DataFrame(
    np.random.rand(100, 2)/(50, 50) + (35.69, 139.70),
    columns=['lat', 'lon']
)

if st.checkbox('Map'):
    st.map(df)

left_column, right_column = st.columns(2)
button = left_column.button('push')
if button:
    right_column.write('here is right column')

expandar1 = st.expander('question a')
expandar1.write('answer 1')
expandar1.write('answer 1a')
expandar1.write('answer 1b')
expandar2 = st.expander('question b')
expandar2.write('answer 2')
expandar3 = st.expander('question c')
expandar3.write('answer 3')

option = st.selectbox(
    'select your favorite number',
    list(range(1, 11))
)
'your favorite number is', option, '.'

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='landscape', use_container_width =True)

text = st.text_input('enter your hobby')
'Your hobby: ', text

condition = st.slider('condition', 0, 100, 50,)
'Condition: ', condition

st.write('')
st.write('progress bar')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration: {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)