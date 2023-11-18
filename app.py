import streamlit as st
import pickle
import pandas as pd

similarity = pickle.load(open('similarity.pkl', 'rb'))
musics = pd.DataFrame(pickle.load(open('data.pkl', 'rb')))


def recommend(movie):
    global musics, similarity
    index = musics[musics['title'] == movie].index[0]
    distances = similarity[index]
    musics_with_index = list(enumerate(distances))
    musics_list = sorted(musics_with_index, reverse=True,
                         key=lambda x: x[1])[1:6]
    recommended_musics = []
    for i in musics_list:
        music = musics.iloc[i[0]]
        recommended_musics.append(f'{music.artist} - {music.title}')
    return recommended_musics


st.title('Music Recommender System')
selected_music = st.selectbox(
    'Select the music',
    musics['artist'].values + ' - '+musics['title'].values
)

if st.button('Recommend'):
    title = selected_music.split("- ", 1)[1]
    print(title)
    recommendations = recommend(title)
    for i in recommendations:
        st.write(i)
