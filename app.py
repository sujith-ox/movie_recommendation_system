import streamlit as st
import pickle
import pandas as pd

# Load data
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))


# Recommendation function
def recommend(movie):
    if movie not in movies["title"].values:
        return []

    idx = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True
    )[1:6]

    return [movies.iloc[i[0]].title for i in distances]


# ---------------------- Streamlit UI ----------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.markdown(
    """
    <style>
    .title {
        font-size:36px;
        font-weight:bold;
        color:#2c3e50;
        text-align:center;
    }
    .subtitle {
        font-size:18px;
        color:#7f8c8d;
        text-align:center;
        margin-bottom:30px;
    }
    .card {
        padding: 20px;
        border-radius: 12px;
        background-color: #f9f9f9;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: 10px;
        text-align:center;
    }
    .movie-title {
        font-size:20px;
        font-weight:600;
        color:#34495e;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='title'>Movie Recommender</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Discover movies similar to your favourites</div>",
    unsafe_allow_html=True,
)

# Dropdown for movie selection
selected_movie = st.selectbox("🎥 Select a movie", movies["title"].values)

# Show recommendations
if st.button("Show Recommendations"):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.subheader("Top Picks for You")
        cols = st.columns(len(recommendations))  # Show in row layout
        for col, movie in zip(cols, recommendations):
            with col:
                st.markdown(
                    f"<div class='card'><div class='movie-title'>{movie}</div></div>",
                    unsafe_allow_html=True,
                )
    else:
        st.warning("No recommendations found. Try another movie.")
