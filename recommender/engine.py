from sklearn.metrics.pairwise import cosine_similarity

def build_candidate_profile(job_role, skills):
    job_role = job_role.lower()
    skills = skills.lower().replace(",", " ")
    
    # Pondération implicite du poste
    return f"{job_role} {job_role} {skills}"

class JobRecommender:

    def __init__(self, df, vectors, vectorizer):
        self.df = df
        self.vectors = vectors
        self.vectorizer = vectorizer

    def recommend(
        self,
        job_role,
        skills,
        top_n=10,
        country=None,
        job_type=None,
        job_level=None
    ):
        profile_text = build_candidate_profile(job_role, skills)
        profile_vector = self.vectorizer.transform([profile_text])

        scores = cosine_similarity(profile_vector, self.vectors)[0]
        results = self.df.copy()
        results["matching_score"] = scores

        # 🎯 Personnalisation intelligente (pondération)
        if country:
            results.loc[
                results["country"].str.lower() != country.lower(),
                "matching_score"
            ] *= 0.6

        if job_type:
            results.loc[
                results["job_type"].str.lower() != job_type.lower(),
                "matching_score"
            ] *= 0.5

        if job_level:
            results.loc[
                results["job_level"].str.lower() != job_level.lower(),
                "matching_score"
            ] *= 0.7

        return results.sort_values(
            "matching_score", ascending=False
        ).head(top_n)
