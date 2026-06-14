import pickle
import streamlit as st
import requests
import pandas as pd
import numpy as np

# -------------------- TMDB APIs --------------------
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
BASE_URL = "https://api.themoviedb.org/3/movie/"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"


def fetch_movie_details(movie_id):
    """
    Fetches the homepage and poster URL for a movie from TMDB.
    """
    url = f"{BASE_URL}{movie_id}?api_key={API_KEY}&language=en-US"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        # Homepage
        homepage = data.get("homepage", "")
        if not homepage:
            homepage = "Homepage not available"

        # Poster
        poster_path = data.get("poster_path")
        if poster_path:
            poster_url = IMAGE_BASE_URL + poster_path
        else:
            poster_url = None

        return homepage, poster_url

    except Exception:
        return "Homepage not available", None


def recommend(movie):
    """
    Returns:
        - Recommended movie names
        - Homepage links
        - Poster URLs
    """
    index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_homepages = []
    recommended_movie_posters = []

    # Top 5 recommendations (excluding the selected movie)
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id

        homepage, poster = fetch_movie_details(movie_id)

        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_homepages.append(homepage)
        recommended_movie_posters.append(poster)

    return (
        recommended_movie_names,
        recommended_movie_homepages,
        recommended_movie_posters,
    )


# -------------------- Streamlit UI --------------------

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommender System")

# Load data
movies = pickle.load(open("movies.pkl", "rb"))
movies = pd.DataFrame(movies)

# Load

with open("similarity.pkl", "rb") as f:

    similarity = pickle.load(f)

print(similarity.dtype)

# Convert to float32

similarity = similarity.astype(np.float32)

# Save again

with open("similarity.pkl", "wb") as f:

    pickle.dump(similarity, f)

# similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

if st.button("Show Recommendations"):

    (
        recommended_movie_names,
        recommended_movie_homepages,
        recommended_movie_posters,
    ) = recommend(selected_movie)

    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:

            st.subheader(recommended_movie_names[i])

            # Display poster
            if recommended_movie_posters[i]:
                st.image(
                    recommended_movie_posters[i],
                    use_container_width=True
                )
            else:
                st.write("Poster not available")

            # Display homepage link
            if recommended_movie_homepages[i] != "Homepage not available":
                st.markdown(
                    f"**[🔗 Visit Homepage]({recommended_movie_homepages[i]})**"
                )
            else:
                st.write("Homepage not available")