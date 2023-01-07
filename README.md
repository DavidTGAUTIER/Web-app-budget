On crée un environnement virtuel (pour isoler et éviter les problèmes de dependances entre librairies)
> python -m venv .venv

On active l'environnement vituel .venv
> .venv\Scripts\activate.bat

Voici la liste des modules à installer : plotly, streamlit
> pip install plotly
> pip install streamlit

On importe les librairie necessaires
> pip install pipreqs # pour installer les librairies et créer le fichier requirements.txt</br>
> pipreqs --encoding=utf8 # version pipreqs 0.4.11 (actuel en janvier 2023)

# https://www.youtube.com/watch?v=3egaMfE9388&t=275s&ab_channel=CodingIsFun
