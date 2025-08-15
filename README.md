🎬 Movie Recommendation System

This is a content-based movie recommendation system built using Python, FastAPI, and Scikit-learn. It recommends similar movies based on metadata like genres, keywords, tagline, cast, and director using TF-IDF vectorization and cosine similarity.

🚀 Features

Content-based filtering for movie recommendations.

TF-IDF Vectorization to process text data.

Cosine Similarity to find related movies.

Fuzzy matching for user input using difflib.

REST API built with FastAPI.

CORS enabled for frontend integration.

Static frontend support.

📦 Installation

Clone the repository

git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender


Create and activate a virtual environment

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt

▶️ Running the App

Make sure you have movies.csv in the project directory.

Run the FastAPI server:

uvicorn app:app --reload


The API will be available at:

http://127.0.0.1:8000


Interactive API documentation is available at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

📡 API Endpoints
Method	Endpoint	Description
GET	/api/health	Health check for the API.
GET	/api/titles	Autocomplete movie titles.
GET	/api/recommend	Get recommended movies based on a title.
📌 Example Usage

Request:

GET /api/recommend?title=Avatar


Response:

[
  "Avatar: The Way of Water",
  "Guardians of the Galaxy",
  "Star Trek Beyond",
  ...
]

🛠️ Tech Stack

Python

FastAPI

Scikit-learn

Pandas

NumPy

Uvicorn
