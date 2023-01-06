On crée un environnement virtuel (pour isoler et éviter les problèmes de dependances entre librairies)
> python -m venv .venv

On active l'environnement vituel .venv
> .venv\Scripts\activate.bat

On importe les librairie necessaires
> pip install pipreqs # pour installer les librairies et créer le fichier requirements.txt</br>
> pipreqs --encoding=utf8 # version pipreqs 0.4.11 (actuel en janvier 2023)