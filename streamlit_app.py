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
import pandas as pd 
import altair as alt

#creer un chart altair
chart = alt.Chart(data).mark_bar().encode(x='SepalLength' , y='SepalWidth')

#afficher le chart sur streamlit
st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(data).mark_point().encode(x='SepalLength' , y='PetalLength')

st.altair_chart(chart, use_container_width=True)

# import streamlit as st

# # Title for the main app
# st.title("Main App Area")

# # Title for the sidebar
# st.sidebar.title("Sidebar")

# # Add widgets to the sidebar
# option = st.sidebar.selectbox(
#     "Select an option:",
#     ["Option iris", "Option data", "Option github"]
# )

# # Display selected option
# st.write(f"You selected: {option}")

