import streamlit as st

def app():
    st.title("🧩 Synthèse Multifacteurs")
    st.markdown("""
    Cette dernière page propose une synthèse croisée de tous les indicateurs :

    - APL
    - Pauvreté
    - Mortalité < 65 ans
    - Mortalité > 65 ans

    👉 Objectif : identifier les départements les plus vulnérables sur tous les plans.
    """)
