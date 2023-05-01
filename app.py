import streamlit as st
import pickle
import pandas as pd

similarity = pickle.load(open('similarity.pkl', 'rb'))
musics_dict = pickle.load(open('data.pkl', 'rb'))
musics = pd.DataFrame(musics_dict)


def recommend(movie):
    global musics, similarity
    index = musics[musics['title'] == movie].index[0]
    distances = similarity[index]
    musics_with_index = list(enumerate(distances))
    musics_list = sorted(musics_with_index, reverse=True,
                         key=lambda x: x[1])[1:6]
    recommended_musics = []
    for i in musics_list:
        recommended_musics.append(musics.iloc[i[0]].title)
    return recommended_musics


st.title('Music Recommender System')
selected_music = st.selectbox(
    'Select the music',
    musics['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_music)
    for i in recommendations:
        st.write(i)
