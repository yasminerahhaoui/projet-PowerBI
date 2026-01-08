import streamlit as st
import requests
import pandas as pd
from streamlit_lottie import st_lottie
import time

st.set_page_config(page_title="NEURAL JOB SEEKER 2026", page_icon="🧠", layout="wide")

def load_lottie(url):
    try:
        r = requests.get(url, timeout=2)
        return r.json() if r.status_code == 200 else None
    except: return None

lottie_main = load_lottie("https://assets5.lottiefiles.com/packages/lf20_M9pWvS.json")

st.markdown("""
    <style>
    .stApp {
        background: #c5d8e8;
        background: linear-gradient(90deg, rgba(197, 216, 232, 1) 0%, rgba(178, 178, 235, 1) 35%, rgba(140, 140, 161, 1) 100%);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: #000000;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .changing-text::after {
        content: "";
        animation: changeText 12s infinite;
        color: #000000;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(168, 85, 247, 0.5);
    }

    @keyframes changeText {
        0%, 33% { content: "Trouvez les meilleures opportunités adaptées à votre profil grâce à notre IA"; opacity: 1; }
        34%, 37% { opacity: 0; }
        38%, 66% { content: "DÉCOUVREZ VOTRE POTENTIEL INFINI"; opacity: 1; }
        67%, 70% { opacity: 0; }
        71%, 96% { content: "L'intelligence artificielle au service de votre carrière"; opacity: 1; }
        97%, 100% { opacity: 0; }
    }

    .sub-header {
        text-align: center;
        font-size: 1.4rem;
        min-height: 2rem;
        margin-bottom: 30px;
        color: #e2e8f0;
    }

    .main-container {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 35px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
        margin-top: 10px;
    }

    input, textarea {
        background: rgba(255, 255, 255, 0.95) !important;
        color: #000000 !important;
        border: 2px solid #6366f1 !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }

    /* Bouton Glow */
    .stButton>button {
        background: linear-gradient(90deg, #6366f1, #a855f7);
        color: white !important;
        border: none;
        padding: 18px;
        border-radius: 15px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        width: 100%;
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 35px rgba(168, 85, 247, 0.7);
    }

    .job-card {
        background: rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        border-left: 5px solid #a855f7;
    }
    label {
        color: #000000 !important; 
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5); 
    }

    .main-container:hover label {
        color: #ffffff !important; 
        transition: color 0.4s ease;
    }
          
    label, .stWidgetFormLabel, p, .st-emotion-cache-162961b, [data-testid="stWidgetLabel"] {
        color: #000000 !important;
        font-weight: 600 !important;
        transition: color 0.3s ease;
    }

    .main-container:hover label, 
    .main-container:hover [data-testid="stWidgetLabel"] {
        color: #a855f7 !important;
        text-shadow: 0 0 10px rgba(168, 85, 247, 0.5);
    }

    div[data-testid="stRadio"] label div p {
        color: #0000000 !important;
    }
    
    .main-container:hover div[data-testid="stRadio"] label div p {
        color: #a855f7 !important;
    }

 
    .main-container {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s ease;
    }

    .main-container:hover {
        border: 1px solid #a855f7;
        box-shadow: 0 0 30px rgba(168, 85, 247, 0.3);
    }
   
    </style>
    """, unsafe_allow_html=True)

# 4. EN-TÊTE
st.markdown("<h1 style='text-align: center; font-size: 4.5em; margin-bottom:0;' class='neon-text'>🧠 NEURAL ENGINE</h1>", unsafe_allow_html=True)
st.markdown('<div class="sub-header"><span class="changing-text"></span></div>', unsafe_allow_html=True)

# 5. CORPS DE L'APPLICATION 
col_left, col_right = st.columns([1, 2.2])

with col_left:
    if lottie_main:
        st_lottie(lottie_main, height=180, key="main_anim")
    
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown("### ⚙️ PARAMÈTRES")
    country = st.selectbox("Destination", ["United States", "United Kingdom", "Canada", "Australia"])
    job_type = st.select_slider("Flexibilité", options=["Onsite", "Hybrid", "Remote"])
    job_level = st.radio("Séniorité", ["Associate", "Mid Senior"])
    top_n = st.number_input("Nombre de résultats", 1, 50, 10)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown("### 🎯 VOTRE PROFIL")
    
    role = st.text_input("Poste visé", placeholder="Ex: Lead AI Engineer")
    skills = st.text_area("Expertises (séparez par des virgules)", placeholder="Python, SQL, PyTorch, Azure...", height=150)
    
    s_list = [s.strip() for s in skills.split(",") if s.strip()]
    
    # Indicateur de précision
    if 0 < len(s_list) < 5:
        st.warning(f"⚠️ Précision : Faible ({len(s_list)}/5 compétences)")
    elif len(s_list) >= 5:
        st.success("Signature neuronale complète !")

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("LANCER LA SYNCHRONISATION"):
        if not role or len(s_list) < 5:
            st.error("Veuillez remplir le rôle et au moins 5 compétences.")
        else:
            with st.status("🔍 Analyse du marché global...", expanded=True) as status:
                # Préparation du JSON (doit correspondre exactement à UserInput dans FastAPI)
                payload = {
                    "job_role": role,
                    "skills": ",".join(s_list),
                    "country": country,
                    "job_type": job_type,
                    "job_level": job_level,
                    "top_n": top_n
                }
                
                try:
                 
                    response = requests.post("http://127.0.0.1:8000/recommend", json=payload)
                    
                    if response.status_code == 200:
                        data = response.json()
                        status.update(label="Synchronisation réussie !", state="complete", expanded=False)
                        
                        st.markdown("### 🚀 OPPORTUNITÉS DÉTECTÉES")
                        for job in data:
                           
                            st.markdown(f"""
                                <div class="job-card">
                                    <h3 style="margin:0; color:#000000;">{job.get('job_title')}</h3>
                                    <p style="margin:5px 0; color:#000000; font-weight:bold;">
                                        🏢 {job.get('company')} | 📍 {job.get('job_location')} | 
                                        <span style="color:#000000;">Match {job.get('matching_score', 0):.1f}%</span>
                                    </p>
                                    <p style="font-size:0.9em; opacity:0.7;">Type: {job.get('job_type')} | Niveau: {job.get('job_level')}</p>
                                </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.error(f"Erreur API : {response.status_code}")
                except Exception as e:
                    st.error(f"Erreur de connexion : {e}")

# 6. FOOTER
st.markdown("<br><p style='text-align: center; opacity: 0.4;'>TERMINAL_ID: 0x8892 | NEURAL_V2.5</p>", unsafe_allow_html=True)
