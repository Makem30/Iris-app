import streamlit as st
import pandas as pd 
import altair as alt

# Charger les données
data = pd.read_csv('Iris.csv', delimiter=";") 
#Créer un titre
st.title("Mon premier tableau de bord Streamlit") 
#Afficher les données dans un tableau
#st.table(data)
#Affichage des 5 premières lignes du jeu de doonnées
st.write(data.head())

st.subheader("Aperçu des données")

# Sélecteur d'espèce
species = st.selectbox("Choisissez une espèce", iris['species'].unique())

# Filtrer les données selon l'espèce choisie
filtered_data = data[data['species'] == species]

# Graphique de distribution de la longueur des sépales
st.subheader(f"Distribution de la longueur des sépales pour {species}")
length_chart = alt.Chart(filtered_data).mark_bar().encode(
    alt.X("sepal_length:Q", bin=alt.Bin(maxbins=20)),
    alt.Y("count():Q"),
    tooltip=["sepal_length:Q", "count():Q"]
).properties(width=600, height=400)

st.altair_chart(length_chart, use_container_width=True)

# Graphique de distribution de la largeur des sépales
st.subheader(f"Distribution de la largeur des sépales pour {species}")
width_chart = alt.Chart(filtered_data).mark_bar().encode(
    alt.X("sepal_width:Q", bin=alt.Bin(maxbins=20)),
    alt.Y("count():Q"),
    tooltip=["sepal_width:Q", "count():Q"]
).properties(width=600, height=400)

st.altair_chart(width_chart, use_container_width=True)

# Graphique de dispersion
st.subheader(f"Graphique de dispersion pour {species}")
scatter_chart = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x='sepal_length:Q',
    y='sepal_width:Q',
    color='species:N',
    tooltip=['sepal_length', 'sepal_width', 'species']
).properties(width=600, height=400)

st.altair_chart(scatter_chart, use_container_width=True)

