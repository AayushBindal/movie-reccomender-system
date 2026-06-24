🎬 Movie Recommender System

<img width="1710" height="987" alt="Screenshot 2026-06-24 at 10 04 08 AM" src="https://github.com/user-attachments/assets/6b07077a-bc79-4bd7-bc0a-fa82b99ec774" />

Live deployement Link :- https://mainpy-ffnv6tnyxnguuafc9hjeep.streamlit.app/

A content-based movie recommendation system built using Python, Streamlit, and Machine Learning. Select a movie from the dropdown, and the application recommends five similar movies along with their posters and official homepage links.

🚀 Features

* 🎥 Content-based movie recommendations
* 🖼️ Displays movie posters using the TMDB API
* 🔗 Provides official homepage links for recommended movies
* ⚡ Fast recommendations using a precomputed similarity matrix
* 🌐 Interactive web interface built with Streamlit

📂 Project Structure

movie-recommender-system/
│── main.py                 # Streamlit application
│── movies.pkl              # Processed movie dataset
│── similarity.pkl          # Precomputed similarity matrix
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation

🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Requests
* TMDB API

📦 Installation

1. Clone the repository:

git clone https://github.com/AayushBindal/movie-reccomender-system.git
cd movie-reccomender-system

2. Create a virtual environment (optional but recommended):

python -m venv .venv

3. Activate the virtual environment:

macOS/Linux

source .venv/bin/activate

Windows

.venv\Scripts\activate

4. Install dependencies:

pip install -r requirements.txt

▶️ Running the Application

Start the Streamlit server:

streamlit run main.py

Then open the URL shown in your terminal.

🎯 How It Works

1. The user selects a movie from the dropdown.
2. The application finds the selected movie in the dataset.
3. A precomputed cosine similarity matrix is used to identify the most similar movies.
4. For each recommendation:
    * The movie title is displayed.
    * The poster is fetched from the TMDB API.
    * The official homepage link is retrieved from TMDB (if available).

📊 Dataset

The recommendation engine uses a processed movie dataset stored in movies.pkl and a precomputed similarity matrix stored in similarity.pkl.

🔑 TMDB API

Movie posters and homepage information are fetched using The Movie Database (TMDB) API.

You will need your own TMDB API key if you wish to modify or extend the project.

🚀 Future Improvements

* Search by actor, director, or genre
* Hybrid recommendation system
* User authentication and watchlists
* Movie trailers integration
* Better UI and animations
* Pagination for more recommendations

👨‍💻 Author

Aayush Bindal

GitHub: https://github.com/AayushBindal

📄 License

This project is intended for educational and learning purposes.
