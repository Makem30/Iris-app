import streamlit as st
import pandas as pd 
# Charger les données
data = pd.read_csv('Iris.csv', delimiter=";") 
#Créer un titre
st.title("Mon premier tableau de bord Streamlit") 
#Afficher les données dans un tableau
#st.table(data)
#Affichage des 5 premières lignes du jeu de doonnées
st.write(data.head())
st.write(count_list = [(df.Species == 'setosa').sum(), (df.Species == 'versicolor').sum(), (df.Species == 'virginica').sum()]
label_list = list(df['Species'].unique())
plt.figure(figsize = (10, 7))
plt.pie(count_list, labels = label_list, autopct = "%.2f %%", startangle = 90, explode = (0.1, 0.1, 0.1), textprops = {'fontsize': 8}, colors=['gold', 'orchid', 'green', "#77BFE2"])
plt.title('Distribution des Classes', fontsize = 30)
plt.show())
