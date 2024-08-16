## Hello Tout le monde bienvenu dans notre projet de blog TECH4ALL

Commencer par telecharger le format compresser et decompresser le dans le repertoire que vous voulez ou
#### cloner le depot en faisant ceci
```bash
git clone https://github.com/drbea/tech4all.git
```

#### ensuite placez vous dans le repertoire tech4all
```bash
cd tech4all
```

#### creer un environement virtuel et activez le
  ## Sous linux
  ### creer avec
  ```bash
  python -m venv virtualEnvName
  ```
  ### activer avec
  
  ```bash
  source virtualEnvName/bin/activate
  ```

  ## Sous Windows
  ### creer avec
  ```bash
  python -m venv virtualEnvName
  ```
  ### activer avec
  
  ```bash
  virtualEnvName/Scripts/activate
  ```

Une fois votre environnement virtuel est en marche quand vous l'activez:
#### installer les dependances du project en faisant ceci
```bash
pip install -r requirements.txt
```
cette commande installera django et et ssa suite pour notre projet
maintenant
Lancer le serveur de developpement django 

###### si vous etes toujours dans le repertoire racine 'tech4all'
```bash
python backend/manage.py runserver
```

ou si voulez vous placer dans le dossier backend faites:
```bash
python manage.py runserver
```
