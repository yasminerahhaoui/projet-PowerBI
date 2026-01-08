***Créer un environnement virtuel (pour isoler les bibliothèques du projet) :
  python -m venv venv 

***Activer l'environnement :
  .\venv\Scripts\activate

***Installer les dépendances :
  pip install streamlit requests pandas streamlit-lottie



***Terminal 1 : Le Serveur (Backend)
L'API doit être lancée en premier car elle contient toute l'intelligence de calcul.

  .\venv\Scripts\activate
  uvicorn api:app --reload

***Terminal 2 : L'Interface (Frontend)
Une fois l'API active, lancez l'interface visuelle.
  streamlit run app.py
