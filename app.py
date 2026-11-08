import streamlit as st
import pandas as pd
import plotly.express as px
from database.repository import get_taux_data, ajouter_alerte, get_alertes_actives
from services.exchange_calculations import calculer_variation, calculer_moyenne

st.set_page_config(page_title="DeviseTrack Pro", page_icon="💱", layout="wide")

st.title("DeviseTrack Pro")
st.write("Bienvenue sur l'outil d'analyse des taux de change.")

try:
    df = get_taux_data()
    
    if df.empty:
        st.warning("La base de données est vide. Veuillez lancer le script API d'abord.")
    else:
        # --- BARRE LATÉRALE ---
        st.sidebar.header("Filtres")
        liste_devises = sorted(df['devise'].unique())
        devise_choisie = st.sidebar.selectbox("Choisissez une devise", liste_devises)
        
        # Formulaire d'alerte
        st.sidebar.markdown("---")
        st.sidebar.header("Créer une alerte")
        with st.sidebar.form("form_alerte"):
            devise_alerte = st.selectbox("Devise ciblée", liste_devises)
            type_alerte = st.radio("Condition", ["Supérieur à", "Inférieur à"])
            seuil = st.number_input("Seuil", value=1.0, step=0.01)
            submit = st.form_submit_button("Enregistrer l'alerte")
            
            if submit:
                ajouter_alerte(devise_alerte, seuil, type_alerte)
                st.sidebar.success("Alerte enregistrée !")
        
        # --- PAGE PRINCIPALE ---
        df_filtre = df[df['devise'] == devise_choisie].sort_values('date')
        
        dernier_taux = df_filtre['taux'].iloc[-1]
        premier_taux = df_filtre['taux'].iloc[0]        
        moyenne = calculer_moyenne(df_filtre['taux'].tolist())
        variation = calculer_variation(premier_taux, dernier_taux)
        
        st.subheader(f"Indicateurs Clés : 1 EUR = ? {devise_choisie}")
        col1, col2, col3, col4 = st.columns(4)
        
        col1.metric("Taux Actuel", f"{dernier_taux:.4f} {devise_choisie}")
        col2.metric("Moyenne (30j)", f"{moyenne:.4f} {devise_choisie}")
        col3.metric("Variation", f"{variation:+.2f} %")
        col4.metric("Jours analysés", len(df_filtre))
        
        st.subheader(f"Évolution de 1 EUR face au {devise_choisie}")
        fig = px.line(df_filtre, x='date', y='taux', title=f"1 EUR = X {devise_choisie}")
        
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title=f"Taux ({devise_choisie})",
            template="plotly_dark"
        )
        
        st.plotly_chart(fig, width='stretch')

        # --- SECTION ALERTES ---
        st.markdown("---")
        st.subheader("Vos alertes enregistrées")
        
        alertes_df = get_alertes_actives()
        
        if not alertes_df.empty:
            st.dataframe(alertes_df[['devise', 'type_alerte', 'seuil']], use_container_width=True)
            
            for index, row in alertes_df.iterrows():
                if row['devise'] == devise_choisie:
                    if row['type_alerte'] == "Supérieur à" and dernier_taux > row['seuil']:
                        st.error(f"ALERTE DÉCLENCHÉE : L'EUR est supérieur à {row['seuil']} {devise_choisie} ! (Taux actuel : {dernier_taux:.4f})")
                    elif row['type_alerte'] == "Inférieur à" and dernier_taux < row['seuil']:
                        st.error(f"ALERTE DÉCLENCHÉE : L'EUR est inférieur à {row['seuil']} {devise_choisie} ! (Taux actuel : {dernier_taux:.4f})")
        else:
            st.info("Aucune alerte enregistrée pour le moment.")

except Exception as e:
    st.error(f"Erreur de connexion : {e}")