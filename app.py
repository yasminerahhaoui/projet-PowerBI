from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from recommender.engine import JobRecommender  # (au lieu de recommender.recommender)
from recommender.preprocessing import build_combined_text
from recommender.vectorizer import train_vectorizer

# =============================
# CHARGEMENT DES DONNÉES ET INITIALISATION
# =============================
# Charger le dataset propre
df = pd.read_excel("data/data_clean (2).xlsx")

# Préparer le texte combiné pour la vectorisation
df = build_combined_text(df)

# Entraîner le vectoriseur et transformer les offres
vectorizer, vectors = train_vectorizer(df["combined_text"])

# Initialiser le moteur de recommandation
engine = JobRecommender(df, vectors, vectorizer)

# =============================
# FASTAPI
# =============================
app = FastAPI(title="Job Recommendation API")

# =============================
# INPUT UTILISATEUR
# =============================
class UserInput(BaseModel):
    job_role: str
    skills: str
    country: str = None
    job_type: str = None
    job_level: str = None
    top_n: int = 10

# =============================
# RECOMMANDATION
# =============================
@app.post("/recommend")
def recommend_jobs(user: UserInput):
    # Appeler le moteur de recommandation
    results = engine.recommend(
        job_role=user.job_role,
        skills=user.skills,
        top_n=user.top_n,
        country=user.country,
        job_type=user.job_type,
        job_level=user.job_level
    )

    # Sélectionner les colonnes à retourner
    output_columns = [
        "job_title", "company", "job_location", 
        "job_type", "job_level", "country", "matching_score"
    ]
    
    return results[output_columns].to_dict(orient="records")

# =============================
# HEALTH CHECK
# =============================
@app.get("/health")
def health():
    return {"status": "ok"}