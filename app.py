import streamlit as st
import pandas as pd
import numpy as np

st.title('Movie Recommender System')

def recommend1(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True,key=lambda x:x[1])[1:6]
    recommended_movie_names = [new_df.iloc[i[0]].title for i in movies_list]
    return recommended_movie_names
new_df= pd.read_csv('new_df.csv')
similarity = pd.read_csv('similarity.csv', header=None).values  # Ensure correct format

movie_list = new_df['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend1(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
    with col2:
        st.text(recommended_movie_names[1])
    with col3:
        st.text(recommended_movie_names[2])
    with col4:
        st.text(recommended_movie_names[3])
    with col5:
        st.text(recommended_movie_names[4])
