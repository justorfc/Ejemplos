import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 2, 100)
y1 = x**3 + 5 * x**2 + 10
y2 = 3*x**2 + 10*x
y3 = 6*x + 10

fig, ax = plt.subplots()

ax.plot(x, y1, color = "blue", label="y(x)=x**3 + 5 * x**2 + 10")
ax.plot(x,y2, color="red", label="y'(x)=3*x**2 + 10*x")
ax.plot(x,y3, color="green", label="y''(x)=6*x + 10")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()

# Mostrar la figura en Streamlit
st.pyplot(fig)