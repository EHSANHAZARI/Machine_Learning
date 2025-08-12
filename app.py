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


# Get the path of the csv file 
DATA_PATH = Path("data/movies.csv")

#Read the data from the file 
df = pd.read_csv(DATA_PATH, encoding="utf-8");



