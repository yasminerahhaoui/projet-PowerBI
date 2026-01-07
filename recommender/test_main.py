from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Maintenant, il trouvera votre fichier app.py
client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_recommend():
    sample_data = {
        "job_role": "Data Scientist",
        "skills": "Python, SQL, Machine Learning",
        "country": "United States",
        "job_type": "Onsite",
        "top_n": 5
    }

    response = client.post("/recommend", json=sample_data)
    assert response.status_code == 200
    json_data = response.json()

    # Affichage pour débogage
    if len(json_data) > 0:
        print(f"✅ Top Recommandation: {json_data[0]['job_title']} chez {json_data[0]['company']}")
    
    assert isinstance(json_data, list)
    assert "matching_score" in json_data[0]