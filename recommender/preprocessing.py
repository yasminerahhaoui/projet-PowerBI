def build_combined_text(df):
    df["combined_text"] = (
        df["job_title"].fillna("") + " " +
        df["job_skills"].fillna("") + " " +
        df["job_summary"].fillna("") + " " +
        df["job_level"].fillna("") + " " +
        df["job_type"].fillna("") + " " +
        df["country"].fillna("")
    )
    return df
