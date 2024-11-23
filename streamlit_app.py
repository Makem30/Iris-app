import streamlit as st
import pandas as pd 
import altair as alt
import numpy as np

# Charger les données
data = pd.read_csv('Iris.csv', delimiter=";") 


#Afficher les données dans un tableau
#st.table(data)
#Affichage des 5 premières lignes du jeu de doonnées
#st.write(data.head())
import pandas as pd 
import altair as alt


# Create two columns
col1, col2 = st.columns([0.7,0.5],gap="large")  

# Content for the first column
with col1:
    
    chart = alt.Chart(data).mark_bar().encode(x='SepalLength' , y='SepalWidth').properties(
    title='Sepal Histogramme')

#afficher le chart sur streamlit
    st.altair_chart(chart, use_container_width=True)
    # st.altair_chart(chart, use_container_width=True)  # Example: Display chart in col1

   
    

# Content for the second column
with col2:
    
    data_aggregated = data.groupby('Species').size().reset_index(name='count')
            
            # 2. Create the Donut Chart
    donut_chart = alt.Chart(data_aggregated).mark_arc(innerRadius=50).encode(
    theta='count:Q',  # Angle of the donut slice (based on 'count')
    color='Species:N',  # Color of the slice (based on 'Species')
    tooltip=['Species:N', 'count:Q']  # Tooltip shows Species and count
    ).properties(
    title='Distribution des espèces dans la Dataset',
    width=400,
    height=400
            )
            
            # 3. Display the chart in Streamlit
    st.altair_chart(donut_chart, use_container_width=True)
    


with st.sidebar:
    st.title('DASHBOARD')




import altair as alt
import streamlit as st
import pandas as pd

# Assuming 'data' is your Pandas DataFrame (e.g., the Iris dataset)

# 1. Aggregate data for the Donut Chart (if needed)
# If your data is not already aggregated (e.g., counts per category), 
# you might need to aggregate it first.
# For example, if you want to show the distribution of 'Species', you could:
chart = alt.Chart(data).mark_point().encode(x='SepalLength' , y='PetalLength').properties(
    title='Sepal et Petal')


st.altair_chart(chart, use_container_width=True)

#----------------------------------------

# chargement de la dataset
data = pd.read_csv('Iris.csv', delimiter=";")

# Sidebar for selecting comparisons
st.sidebar.header("Comparaison des fleurs")

# Flower species selection
species_options = data['Species'].unique().tolist()
selected_species = st.sidebar.multiselect(
    "Selectionnez les espèces à comparer:", species_options, default=species_options[:2]
)

# Feature selection
feature_options = ['PetalWidth', 'SepalWidth', 'PetalLength', 'SepalLength']
x_feature = st.sidebar.selectbox("X-axe Caractéristiques:", feature_options, index=0)
y_feature = st.sidebar.selectbox("Y-axe Caractéristiques:", feature_options, index=1)

# Filter data based on selected species
filtered_data = data[data['Species'].isin(selected_species)]

# Create the chart
chart = alt.Chart(filtered_data).mark_point().encode(
    x=alt.X(x_feature, scale=alt.Scale(zero=False)),  # Adjust scale if needed
    y=alt.Y(y_feature, scale=alt.Scale(zero=False)),
    color='Species:N'
).properties(
    title=f"Comparison of {x_feature} vs {y_feature}"
)

# Display the chart
st.altair_chart(chart, use_container_width=True)

#----------------creation des colonnes----------------------------------------
# ... (your previous code for data loading and sidebar) ...









