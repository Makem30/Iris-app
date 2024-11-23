import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np

# Charger les données
data = pd.read_csv('Iris.csv', delimiter=";") 
#Créer un titre
st.title("Sepal Histogramme") 
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
st.title("Sepal et Petal") 

chart = alt.Chart(data).mark_point().encode(x='SepalLength' , y='PetalLength')

st.altair_chart(chart, use_container_width=True)

import streamlit as st

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

with st.sidebar:
    st.title('Dashboard')




import altair as alt
import streamlit as st
import pandas as pd

# Assuming 'data' is your Pandas DataFrame (e.g., the Iris dataset)

# 1. Aggregate data for the Donut Chart (if needed)
# If your data is not already aggregated (e.g., counts per category), 
# you might need to aggregate it first.
# For example, if you want to show the distribution of 'Species', you could:
data_aggregated = data.groupby('Species').size().reset_index(name='count')

# 2. Create the Donut Chart
donut_chart = alt.Chart(data_aggregated).mark_arc(innerRadius=50).encode(
    theta='count:Q',  # Angle of the donut slice (based on 'count')
    color='Species:N',  # Color of the slice (based on 'Species')
    tooltip=['Species:N', 'count:Q']  # Tooltip shows Species and count
).properties(
    title='Distribution of Species in Iris Dataset',
    width=400,
    height=400
)

# 3. Display the chart in Streamlit
st.altair_chart(donut_chart, use_container_width=True)





