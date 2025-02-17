import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = np.random.rand(200,1) 
y = np.random.rand(200,1)
z = np.random.rand(200,1)

ax.scatter(x, y, z, s=40, c="blue")
# ax.plot_surface(x, y, z,color="lightgreen", rcount=100, ccount=100, antialiased=False)
# plt.show()

st.pyplot(fig)