import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.graph_objects as go
from PIL import Image

st.title('Streamlit Samples')
st.write('Interactive Wedgets')

if st.checkbox('Table'):
    df = pd.DataFrame({
    '1st row': [1, 2, 3, 4, 5],
    '2nd row': [10, 20, 30, 40, 50]
    })
    st.write(df)

if st.checkbox('Graphs'):
    df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
    )
    st.line_chart(df)
    st.area_chart(df)
    st.bar_chart(df)
    
if st.checkbox('Map'):
    df = pd.DataFrame(
    np.random.rand(100, 2)/(50, 50) + (35.69, 139.70), 
    columns=['lat', 'lon']
    ) 
    st.map(df)

if st.checkbox('Multi column'):
    left_column, right_column = st.columns(2)
    button = left_column.button('push')
    if button:
        right_column.write('here is right column')

if st.checkbox('Expander'):
    expandar1 = st.expander('question a')
    expandar1.write('answer 1')
    expandar1.write('answer 1a')
    expandar1.write('answer 1b')
    expandar2 = st.expander('question b')
    expandar2.write('answer 2')
    expandar3 = st.expander('question c')
    expandar3.write('answer 3')

if st.checkbox('Select box'):
    option = st.selectbox(
        'select your favorite number',
        list(range(1, 11))
    )
    'your favorite number is', option, '.'

if st.checkbox('Show image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='landscape', use_container_width =True)

if st.checkbox('Input text'):
    text = st.text_input('Enter text')
    'Your input: ', text

if st.checkbox('Slider'):
    condition = st.slider('Condition', 0, 100, 50,)
    'Condition: ', condition

if st.checkbox('Sidebar'):
    text = st.sidebar.text_input('Enter text')
    st.sidebar.write('Your input: ', text)
    condition = st.sidebar.slider('Condition', 0, 100, 50,)
    st.sidebar.write('Condition: ', condition)

if st.checkbox('Progress bar'):
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Iteration: {i+1}')
        bar.progress(i + 1)
        time.sleep(0.05)

if st.checkbox('Sphere'):
    u = np.linspace(0, 2*np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    ax = 10 * np.outer(np.cos(u), np.sin(v))
    ay = 10 * np.outer(np.sin(u), np.sin(v))
    az = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
    fig = go.Figure(data = [go.Surface(x = ax, y = ay, z = az)])
    fig.update_layout(title = dict(text='Sphere'), autosize=False,
                width=500, height=500,
                margin = dict(l=65, r=50, b=65, t=90))
    st.plotly_chart(fig)
