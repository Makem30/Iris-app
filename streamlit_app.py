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

# col = st.columns((1.5,4.5,2), gap = 'medium')
# with col[0]:
    st.markdown('diagramme secteur')
    
    # Créer le diagramme sectoriel
pie_chart = alt.Chart(data).mark_arc().encode(x='SepalLength' , y='SepalWidth').properties(
    title='Distribution des espèces dans le jeu de données Iris',
    width=300,
    height=300
)

# Afficher le diagramme sectoriel sur Streamlit
st.title("Dashboard Iris avec Diagramme Sectoriel")
st.altair_chart(pie_chart, use_container_width=True)




import streamlit as st
from keras.models import load_model 
import numpy as np 

model = load_model("model.h5")
labels = np.load("labels.npy") 

st.title("Iris flower prediction app")

a = float(st.number_input("sepal length in cm"))
b = float(st.number_input("sepal width in cm"))
c = float(st.number_input("petal length in cm"))
d = float(st.number_input("petal width in cm"))

btn = st.button("predict")

if btn:
	pred = model.predict(np.array([a,b,c,d]).reshape(1,-1))
	pred = labels[np.argmax(pred)]
	st.subheader(pred)

	if pred=="Setosa":
		st.image("setosa.jpg")
	elif pred=="Versicolour":
		st.image("versicolor.jpg")
	else:	
		st.image("verginca.jpg")

