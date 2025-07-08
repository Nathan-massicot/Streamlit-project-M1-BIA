import streamlit as st

def app():
    st.title("🏥 Introduction à l'APL (Accessibilité Potentielle Localisée)")

    st.markdown("""
    L’indicateur **APL** mesure l’adéquation spatiale entre l’offre de soins en médecine générale et la demande locale, 
    à un niveau géographique fin. Il est essentiel pour identifier les déserts médicaux et planifier les politiques de santé publique.

    Ce tableau de bord vous propose une exploration progressive du lien entre :
    - l’APL,
    - la mortalité avant 65 ans,
    - la mortalité après 65 ans,
    - et le taux de pauvreté.

    ---

    ### ℹ️ D'où vient l'indicateur APL ?

    L’APL utilisé ici est une **valeur déjà calculée** au niveau départemental, extraite de sources publiques (ex. DREES, Insee).

    Il repose sur la méthode dite **"Two-Step Floating Catchment Area" (2SFCA)**, qui évalue à la fois :
    - l’offre de médecins dans un périmètre donné (ex : 30 min de route),
    - la demande locale de soins (population),
    - et la distance d’accès (pondérée par une fonction de décroissance).

    La formule simplifiée est :

    $$
    APL_i = \\sum_{j \\in J} \\left( \\frac{S_j}{\\sum_{k \\in K} P_k \\cdot f(d_{kj})} \\cdot f(d_{ij}) \\right)
    $$

    - \( S_j \) : capacité d'un professionnel (consultations annuelles)
    - \( P_k \) : population dans une zone autour de chaque médecin
    - \( f(d) \) : fonction qui pénalise la distance

    ---

    ### 🧭 Schéma explicatif

    ![Schéma APL 2SFCA](https://raw.githubusercontent.com/openhealthcare/2sfca-diagram/main/2sfca_method.png)

    (Ce schéma illustre le principe de l’accessibilité potentielle localisée à partir des bassins de soins.)
    """)