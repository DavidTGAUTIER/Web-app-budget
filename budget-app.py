import calendar
import datetime
import streamlit as st
import plotly.graph_objects as go


# --------------------------------- SETTINGS ---------------------------------------
revenus = ['Salaire', 'Blog', 'Autre revenu']
depenses = ['Location', 'Charges', 'Course', 'Voiture', 'Economie', 'Autre dépense']
devise = "€"
titre = "Tracker de revenus et de dépenses"
icon = ":money_with_wings:" # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# -----------------------------------------------------------------------------------

st.set_page_config(page_title=titre, page_icon=icon, layout=layout)
st.title(titre + " " + icon)

#------------- VALEURS DU MENU DEROULANT POUR SELECTIONNER UNE PERIODE --------------
annees = [datetime.today().year, datetime.today().year+1]
mois = ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
# months = list(calendar.month_name[1:])

#------------------------- ENTREES & SAUVEGARDE DES PERIODES ------------------------
st.header(f"Entrée des données en {devise}")
with st.form("Format d'entrée", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Selectionner un mois:", mois, key="mois")
    col2.selectbox("Selectionner une année:", annees, key="année")


