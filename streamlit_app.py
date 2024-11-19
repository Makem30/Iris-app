import streamlit as st
import pandas as pd 
import altair as alt

# Charger les données
data = pd.read_csv('Iris.csv', delimiter=";") 
#Créer un titre
st.title("Dashboard Streamlit") 
#Afficher les données dans un tableau
#st.table(data)
#Affichage des 5 premières lignes du jeu de doonnées
#st.write(data.head())

#creer un chart altair
chart = alt.Chart(data).mark_bar().encode(x='SepalLength' , y='SepalWidth')

#afficher le chart sur streamlit
st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(data).mark_point().encode(x='SepalLength' , y='PetalWidth')

with st.sidebar:
    st.[element_name]

#affiche la chart sur streamlit
st.altair_chart(chart, use_container_width=True)

with st.sidebar:
    st.[st.title("Dashboard Streamlit")]

