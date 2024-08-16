#  TECH4ALL Blog
## A. Description

TECH4ALL Blog est un projet de blog d'entreprise développé avec Django et Bootstrap. Il est conçu pour promouvoir les services de l'entreprise, informer les clients, et renforcer la marque à travers des articles pertinents et engageants.
### A.1. Fonctionnalités

    Page d'accueil élégante : Comprend une barre de navigation avec le logo RAS TECH, une barre de recherche intégrée, et des liens de navigation vers les sections principales.
    Barres latérales (sidebars) :
        Sidebar gauche : Contient les liens vers les différents services de l'entreprise.
        Sidebar droit : Affiche les activités récentes du blog, comme les nouveaux articles ou mises à jour importantes.
    Articles de blog : Les articles sont classés en catégories pour une navigation facile et sont publiés régulièrement pour maintenir l'engagement des lecteurs.
    Système de commentaires : Permet aux utilisateurs de laisser des commentaires et d'interagir avec les articles.
    Partage sur les réseaux sociaux : Intègre des boutons de partage pour diffuser les articles sur les principales plateformes sociales.
    Design responsive : Utilise Bootstrap pour garantir une expérience utilisateur optimale sur tous les appareils.

### A.2. Technologies utilisées

    Django : Backend du projet, gestion des articles et des commentaires.
    Bootstrap : Pour une mise en page moderne et responsive.
    Font Awesome : Utilisé pour les icônes des réseaux sociaux dans le footer.
    SQLite (par défaut, remplaçable par d'autres bases de données pour la production).

## B. INSTALLATION
Commencer par telecharger le format compresser et decompresser le dans le repertoire que vous voulez ou

### B.1 cloner le depot en faisant ceci
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


## C. notes {ONLY} for linux users
### ou si voulez utliser l'environement envTech qui existe, 
### mais je suis sous linux donc ne l'utiliser que si vous etes sous une distro linux
```git
source .envTech/bin/activate
```
