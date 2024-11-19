import streamlit as st
import pandas as pd 
import plotly.express as px
# Charger les données
data = pd.read_csv('Iris.csv', delimiter=";") 
#Créer un titre
st.title("Mon premier tableau de bord Streamlit") 
#Afficher les données dans un tableau
#st.table(data)
#Affichage des 5 premières lignes du jeu de doonnées
st.write(data.head())



# Assuming you have a Pandas DataFrame 'df' with data for your scatter plot
fig = px.scatter(df, x="SepalLength", y="PetalWidth", color="Species")
st.plotly_chart(data)
