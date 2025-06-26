import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🗽 Roteiro NYC: 02 a 11 de Julho")

@st.cache_data
def carregar_dados():
    return pd.read_csv("pontos_completos.csv")

df = carregar_dados()

dias = [
    ("02/07", "Midtown"),
    ("03/07", "Chelsea + Flatiron"),
    ("04/07", "SoHo/NoHo + Greenwich Village"),
    ("05/07", "East Village + Lower East"),
    ("06/07", "Financial District"),
    ("07/07", "Uptown"),
    ("08/07", "Upper East/West Side"),
    ("09/07", "Outlet - Jersey Gardens"),
    ("10/07", "Dia Livre"),
    ("11/07", "Últimos Passeios")
]

for data, regiao in dias:
    with st.expander(f"📅 {data} — {regiao}"):
        pontos_dia = df[df['Regiao'].str.contains(regiao.split('+')[0].strip(), case=False)]
        st.write(pontos_dia[['Nome', 'Categoria', 'Latitude', 'Longitude']])

        # CORREÇÃO: Só exibe o mapa se houver pontos
        if not pontos_dia.empty:
            st.map(pontos_dia[['Latitude', 'Longitude']])
        else:
            st.warning("Nenhum ponto encontrado para essa região.")

        st.text_area(f"Anotações para {data}", placeholder="Escreva algo...", key=f"nota_{data}")

        if "Rooftop" in regiao or data in ["02/07", "04/07", "05/07", "07/07"]:
            st.markdown("**🌆 Sugestão de rooftop com vista:**")
            st.markdown("- [230 Fifth](https://www.230-fifth.com/)")
            st.markdown("- [The Skylark](https://www.theskylarknyc.com/)")
            st.markdown("- [Westlight (Williamsburg)](https://www.westlightnyc.com/)")
