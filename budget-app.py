import calendar
from datetime import datetime
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
    col1.selectbox('Selectionner un mois:', mois, key='mois')
    col2.selectbox('Selectionner une année:', annees, key='annee')
    "----------------"
    with st.expander("Revenus"):
        for revenu in revenus:
            st.number_input(f'{revenu}:', min_value=0, format='%i', step=10, key=revenu)
    with st.expander("Depenses"):
        for depense in depenses:
            st.number_input(f'{depense}:', min_value=0, format='%i', step=10, key=depense)
    with st.expander('Commentaires'):
        commentaire = st.text_area("", placeholder="Entrez un commentaire ici ...")
    "----------------"
    soumission = st.form_submit_button("Sauvegarde des données")
    if soumission:
        periode = str(st.session_state['annee']) + "_" + str(st.session_state['mois'])
        revenus = {revenu:st.session_state[revenu] for revenu in revenus}
        depenses = {depense:st.session_state[depense] for depense in depenses}
        # TODO : Inserez des valeurs dans la database
        st.write(f'revenus: {revenus}')
        st.write(f'depenses: {depenses}')
        st.success('Données sauvegardées !')

# ----------------------- AFFICHAGE DES GRAPHIQUES DES PERIODES  -----------------------
st.header("Visualisation des données")
with st.form("periodes_sauvegardees"):
    # TODO: Obtenir les périodes depuis la database
    periode = st.selectbox("Selectionnez une période :", ["Mars_2022"])
    soumission = st.form_submit_button("Affichage de la période")
    if soumission:
        # TODO: Obtenir les données depuis la database
        commentaire = "..."
        revenus = {'Salaire':1500, 'Blog':50, 'Autre revenu':10}
        depenses = {'Location':600, 'Charges':300, 'Course':150, 'Voiture':100, 'Economie':50, 'Autre dépense':30}
        # Creation des metriques
        revenus_total = sum(revenus.values())
        depenses_total = sum(depenses.values())
        budget_restant = revenus_total - depenses_total
        col1, col2, col3 = st.columns(3)
        col1.metric("Revenus total", f"{revenus_total} {devise}")
        col2.metric("Depenses total", f"{depenses_total} {devise}")
        col3.metric("Budget restant", f"{budget_restant} {devise}")
        st.text(f"Commentaire: {commentaire}")

# with pleasure
