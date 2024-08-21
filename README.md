Movie Recommender System
Description
This project is a Movie Recommender System built using data from the TMDB (The Movie Database) 5000 dataset. The system recommends movies similar to a given movie by analyzing their metadata, including movie ID, name, overview, genre, cast, keywords, and crew. By creating tags from the genre, cast, keywords, and crew information, the project utilizes a bag-of-words technique and calculates cosine similarity to find and recommend the top 5 movies similar to the selected movie. The project is deployed as an interactive web application using Streamlit.

Folder Structure
movie-recommender-system.ipynb: The Jupyter Notebook containing the code for creating the movie recommender system. It includes the data preprocessing steps, vectorization, and similarity calculation.
tmdb_5000_credits.csv: The dataset containing movie credits (e.g., cast and crew information) used in the recommender system.
tmdb_5000_movies.csv: The dataset containing detailed movie metadata (e.g., movie names, overviews, genres) used in the recommender system.
app.py: The Streamlit application script that serves the movie recommender system as a web app.

Installation Instructions

Clone the repository:
git clone https://github.com/saadkhannust/movie-recommender-system.git

Navigate to the project directory:
cd movie-recommender-system

Install the required dependencies:
pip install -r requirements.txt

Running the Code
Run the Jupyter Notebook:
Open the movie-recommender-system.ipynb to explore the data processing and model creation steps.

Run the Streamlit App:
Navigate to the streamlit_app folder:
cd streamlit_app

Run the Streamlit application:
streamlit run app.py

The app will start in your browser, allowing you to input a movie and receive recommendations.

Contributors
Muhammad Saad Khan



