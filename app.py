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

#Choose the features that we want to assess the data with 
selected_feature = ["keywords" , "genres" , "tagline" , "cast" , "director"]

#Replacing all the missing and non values with empty string to prevent error on concatination 
for col in selected_feature:
    df[col] = df[col].fillna("") #fillna fills all the empty string with being passed to it 

# Combining the features 
combined = (
    df["genres"] + " " + 
    df["keywords"] + " " + 
    df["tagline"] + " " + 
    df["cast"] + " " + 
    df["director"]
).str.lower

#vectorize
vectorizer = TfidfVectorizer(stop_words="english"); #This stops when it reaches to the english words like "This" "There" "is" "a"
feature_matrix = vectorizer.fit_transform(combined) #This is converting the letters to numeric number 




