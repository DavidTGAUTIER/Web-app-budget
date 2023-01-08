#### On crée un environnement virtuel (pour isoler et éviter les problèmes de dependances entre librairies)
> python -m venv .venv

#### On active l'environnement vituel .venv</br>
sous windows:</br>
> .venv\Scripts\activate.bat

sous mac/linux:
> source .venv/bin/activate

#### Voici la liste des modules à installer : `plotly`, `streamlit`
> pip install plotly</br>
> pip install streamlit

#### On importe les librairie necessaires</br>
> pip install pipreqs # pour installer les librairies et créer le fichier
requirements.txt</br>
> pipreqs --encoding=utf8 # version pipreqs 0.4.11 (actuel en janvier 2023)

#### On crée l'image Docker
> docker build . -t budget-web-app

#### On execute l'image Docker</br>
sur windows(localhost) :</br>
> docker run -it -v "%cd%:/home/app" -p 4000:4000 -e PORT=4000 budget-web-app</br>

sur mac / linux(localhost) :</br>
> docker run -it -v "$(pwd):/home/app" -p 4000:4000 -e PORT=4000 budget-web-app

#### Deploiement de l'app : masquer les variables d'environnement</br>
avec Heroku :</br>
> heroku config:set DETA_KEY="XXXXXXXXXXXXXXXXXXXXX"

avec streamlit (https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management):</br> 
> st.secrets["DETA_KEY"])



