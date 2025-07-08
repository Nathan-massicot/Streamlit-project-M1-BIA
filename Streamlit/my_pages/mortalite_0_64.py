import streamlit as st
import pandas as pd
import plotly.express as px
import json

def app():
    st.title("⚰️ APL & Mortalité des moins de 65 ans")

    st.markdown("""
    Cette section explore le lien entre l'accessibilité aux soins et la mortalité prématurée (moins de 65 ans).

    👉 **Hypothèse** : une faible APL pourrait être associée à une mortalité prématurée plus élevée.
    """)

    # Charger les données
    df = pd.read_csv("data/dept_vulnerabilite_2022.csv")

    # Charger le GeoJSON des départements
    with open("data/departements.geojson", "r", encoding="utf-8") as f:
        geojson_dept = json.load(f)

    st.subheader("📍 Carte interactive : mortalité des moins de 65 ans")
    fig_map = px.choropleth(
        df,
        geojson=geojson_dept,
        locations="code_dep",
        featureidkey="properties.code",
        color="mortalite_0_64",
        color_continuous_scale="Reds",
        hover_name="departement",
        labels={"mortalite_0_64": "Taux mortalité < 65 ans"}
    )
    fig_map.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig_map, use_container_width=True)

    st.subheader("📈 Corrélation APL et mortalité < 65 ans")
    fig_scatter = px.scatter(
        df,
        x="apl_med",
        y="mortalite_0_64",
        hover_name="departement",
        trendline="ols",
        labels={
            "apl_med": "Accessibilité potentielle localisée (APL)",
            "mortalite_0_64": "Taux mortalité < 65 ans"
        }
    )
    st.plotly_chart(fig_scatter, use_container_width=True)