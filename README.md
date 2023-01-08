On crée un environnement virtuel (pour isoler et éviter les problèmes de dependances entre librairies)
> python -m venv .venv

On active l'environnement vituel .venv
sous windows:</br>
> .venv\Scripts\activate.bat
sous mac/linux:
> source .venv/bin/activate

Voici la liste des modules à installer : plotly, streamlit
> pip install plotly
> pip install streamlit

On importe les librairie necessaires
> pip install pipreqs # pour installer les librairies et créer le fichier requirements.txt</br>
> pipreqs --encoding=utf8 # version pipreqs 0.4.11 (actuel en janvier 2023)

On crée l'image Docker
> docker build . -t budget-web-app

On execute l'image Docker
sur windows(localhost) : 
> docker run -it -v "%cd%:/home/app" -p 4000:4000 -e PORT=4000 budget-web-app
sur mac / linux(localhost) :
> docker run -it -v "$(pwd):/home/app" -p 4000:4000 -e PORT=4000 budget-web-app

# https://www.youtube.com/watch?v=3egaMfE9388&t=275s&ab_channel=CodingIsFun
