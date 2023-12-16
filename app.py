import streamlit as st
import pickle
import pandas as pd

st.title("Movie Recommendations")

movie_dict = pickle.load(open('Movie_list.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommendations = []
    for movie in movie_list:
        recommendations.append(movies.iloc[movie[0]].title)

    return recommendations

selected_movie_name = st.selectbox("Select a movie to get recommendations" , movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)