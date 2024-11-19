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
Species = st.selectbox("Choisissez une espèce", data['Species'].unique())

# Filtrer les données selon l'espèce choisie
filtered_data = data[data['Species'] == Species]

# Graphique de distribution de la longueur des sépales
st.subheader(f"Distribution de la longueur des sépales pour {Species}")
length_chart = alt.Chart(filtered_data).mark_bar().encode(
    alt.X("SepalLength:Q", bin=alt.Bin(maxbins=20)),
    alt.Y("count():Q"),
    tooltip=["sepal_length:Q", "count():Q"]
).properties(width=600, height=400)

st.altair_chart(length_chart, use_container_width=True)

# Graphique de distribution de la largeur des sépales
st.subheader(f"Distribution de la largeur des sépales pour {Species}")
width_chart = alt.Chart(filtered_data).mark_bar().encode(
    alt.X("SepalWidth:Q", bin=alt.Bin(maxbins=20)),
    alt.Y("count():Q"),
    tooltip=["SepalWidth:Q", "count():Q"]
).properties(width=600, height=400)

st.altair_chart(width_chart, use_container_width=True)

# Graphique de dispersion
st.subheader(f"Graphique de dispersion pour {Species}")
scatter_chart = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x='SepalLength:Q',
    y='SepalWidth:Q',
    color='Species:N',
    tooltip=['SepalLength', 'SepalWidth', 'Species']
).properties(width=600, height=400)

st.altair_chart(scatter_chart, use_container_width=True)

