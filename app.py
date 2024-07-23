import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
data = pd.read_csv(url)

st.write("Dados de exemplo de flor iris")
st.write(data)

st.write("Gráfico de Dispersão")
fig, ax = plt.subplots()


colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
ax.scatter(data["sepal_length"], data["petal_length"], c=data["species"].map(colors))

# ax.scatter(data["sepal_length"], data["petal_length"])
ax.set_xlabel("Comprimento da Sépala")
ax.set_ylabel("Comprimento da Pétala")
st.pyplot(fig)

#colocar cor 
# ordenar por especie e fazer um outro garfico aparecer
# cores para setosa, virginica, versicolor
# separar as espécies 

# streamlit run app.py
# pip install streamlit kiddfyfif
# pip install matplotlib
# streamlit hello
# source venv/bin/activate
# 



