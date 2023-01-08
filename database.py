from deta import Deta
import streamlit as st

# Project Key
DETA_KEY = 

# Initialisation de Deta avec la DETA_KEY
deta = Deta(DETA_KEY)

# Comment creer / connecter à database
db = deta.Base('rapports_mensuel')

"""
Pour inserer un point, on définit quatre paramètres:
* periode (clé = identifiant unique)
* revenus
* depenses
* commentaire
puis on utilise db.put pour les inserer
"""

# Insérer des valeurs d'une période spécifique dans la database
def inserer_period(periode, revenus, depenses, commentaire):
    "Retourne le rapport d'une creation avec succes, sinon renvoi une erreur"
    return db.put({"clé":periode, "revenus":revenus, "depenses":depenses, "commentaire":commentaire})

"""
Pour récupérer toutes les périodes, on utilise 'db.fetch'
Cela renvoi une instance d'une classe FetchResponse avec les propriétés suivantes:
* items (tous les items)
* last (dernier item)
* count (nombre d'items total)
"""

# Recuperer toutes les périodes pour remplir st.selectbox
def cherche_toutes_periodes():
    "Retourne un dictionnaire de toutes les périodes"
    res = db.fetch()
    return res.items

"""
On peut récupérer uniquement une période particulière en utilisant 'db.get'
"""

# Obtenir toutes les valeurs d'une période particulière pour tracer les données
def obtenir_periode(periode):
    "Si pas de période, retourne None"
    return db.get(periode)