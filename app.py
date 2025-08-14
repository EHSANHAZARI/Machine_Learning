from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from typing import List
import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

# ---- Load data ----
DATA_PATH = Path("data/movies.csv")
df = pd.read_csv(DATA_PATH, encoding="utf-8")

selected_feature = ["keywords", "genres", "tagline", "cast", "director"]
for col in selected_feature:
    df[col] = df[col].fillna("")

combined = (
    df["genres"] + " " +
    df["keywords"] + " " +
    df["tagline"] + " " +
    df["cast"] + " " +
    df["director"]
).str.lower()

vectorizer = TfidfVectorizer(stop_words="english")
feature_matrix = vectorizer.fit_transform(combined)
similarity_matrix = cosine_similarity(feature_matrix)  # It makes the process faster 


# CHANGE HERE if your column is 'titles'
title_col = "title"   # or "titles"
titles = df[title_col].fillna("").tolist()
title_to_index = {t: i for i, t in enumerate(titles)}

app = FastAPI(title="Movie Recommender")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "ok"}

def recommend_by_index(idx: int, k: int = 10) -> List[str]:
    sims = similarity_matrix[idx]  # using the premade function 
    order = np.argsort(sims)[::-1]
    order = [i for i in order if i != idx][:k]
    return [titles[i] for i in order]

@app.get("/api/titles", response_model=List[str])
def list_titles(q: str = Query("", description="Partial title for autocomplete")):
    if not q:
        return titles[:100]
    matches = difflib.get_close_matches(q, titles, n=20, cutoff=0.4)
    subs = [t for t in titles if q.lower() in t.lower()]
    seen, out = set(), []
    for t in matches + subs:
        if t not in seen:
            seen.add(t)
            out.append(t)
        if len(out) >= 20:
            break
    return out

@app.get("/api/recommend", response_model=List[str])
def recommend(title: str = Query(..., description="Movie title")):
    if title in title_to_index:
        idx = title_to_index[title]
    else:
        close = difflib.get_close_matches(title, titles, n=1, cutoff=0.4)
        if not close:
            raise HTTPException(status_code=404, detail="No close title found.")
        idx = title_to_index[close[0]]
    return recommend_by_index(idx, k=10)

# Mount static last (optional)
app.mount("/", StaticFiles(directory=".", html=True), name="frontend")
