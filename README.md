Movie Recommendation (Content-Based • FastAPI + TF-IDF)

A lightweight, end-to-end movie recommender that uses TF-IDF and cosine similarity to find titles similar to a user’s input. Backend is built with FastAPI, and a simple frontend is included for quick demos.

✨ Features

Content-based recommendations (genres, keywords, tagline, cast, director)

Fast API endpoints: health check, title suggestions, recommendations

Instant demo UI (vanilla HTML/CSS/JS) or consumable via REST

Ready for deployment to Render/Railway (Docker optional)

Extensible: plug in new features or swap vectorizers

🧱 Tech Stack

Backend: Python, FastAPI, Uvicorn

ML: scikit-learn (TfidfVectorizer, cosine_similarity)

Frontend: HTML, CSS, JavaScript (optional)

Data: movies.csv

🚀 Quickstart
1) Clone & setup
git clone https://github.com/EHSANHAZARI/Movie-Recommendation-ML.git
cd Movie-Recommendation-ML

# (Optional) create virtual env
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

2) Run locally (dev)
uvicorn app:app --reload
# or, if using suggested structure:
uvicorn backend.app:app --reload


Open: http://127.0.0.1:8000

Interactive docs: http://127.0.0.1:8000/docs

JSON schema: http://127.0.0.1:8000/openapi.json

If the frontend is served by FastAPI (StaticFiles), the root / will load index.html.
Otherwise, open frontend/index.html directly (and point API calls to http://127.0.0.1:8000).

🧪 API Endpoints
Health
GET /api/health


200 → {"status":"ok"}

Title suggestions (autocomplete)
GET /api/titles?q=bat


200 → ["Batman Begins","The Dark Knight", ...]

Recommendations
GET /api/recommend?title=The%20Matrix&k=10


200 → ["The Matrix Reloaded", "Dark City", "Equilibrium", ...]

cURL examples
curl http://127.0.0.1:8000/api/health
curl "http://127.0.0.1:8000/api/titles?q=star"
curl "http://127.0.0.1:8000/api/recommend?title=Inception&k=10"

🧠 How It Works

Load dataset (movies.csv) and fill missing values for selected features.

Build a TF-IDF feature space from combined text fields.

At query time, vectorize the input title → compute cosine similarity → return Top-K similar titles.

(Optional) Cache fitted vectorizer/matrix on startup for performance.
