# Gestionnaire de Tournois d'Échecs

Une application Python pour gérer les tournois d'échecs.

## Description

Cette application permet de :
- Gérer une base de données de joueurs
- Créer et gérer des tournois d'échecs
- Générer automatiquement les appariements.
- Enregistrer les résultats des matchs
- Générer différents rapports

## Prérequis

- Python 3.x
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone [url-du-depot]
cd [nom-du-dossier]
```

2. Créez un environnement virtuel et activez-le :
```bash
python -m venv .venv

# Sur Windows :
.venv\Scripts\activate

# Sur macOS/Linux :
source .venv/bin/activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Structure du Projet

```
.
├── data/               # Dossier contenant les données JSON
│   └── tournaments/    # Données des tournois
├── src/               # Code source
│   ├── models/        # Modèles de données
│   ├── views/         # Interface utilisateur
│   ├── controllers/   # Logique de contrôle
│   └── helpers/       # Fonctions utilitaires
├── flake8_rapport/    # Rapport de conformité du code
├── main.py            # Point d'entrée de l'application
├── requirements.txt   # Dépendances Python
└── .flake8           # Configuration flake8
```

## Utilisation

1. Lancez l'application :
```bash
python main.py
```

2. Suivez les instructions du menu principal pour :
   - Gérer les joueurs (ajout, consultation)
   - Gérer les tournois (création, modification, consultation)
   - Consulter les différents rapports

## Génération du Rapport Flake8

Pour générer un nouveau rapport de conformité du code :

```bash
flake8 --format=html --htmldir=flake8_rapport
```

Le rapport sera généré dans le dossier `flake8_rapport`.

## Fonctionnalités

### Gestion des Joueurs
- Ajout de nouveaux joueurs avec :
  - Nom
  - Prénom
  - Date de naissance
  - Identifiant national d'échecs (format : AB12345)

### Gestion des Tournois
- Création de tournois avec :
  - Nom
  - Lieu
  - Dates de début et fin
  - Nombre de tours (par défaut : 4)
  - Description
- Gestion automatique des appariements
- Enregistrement des résultats des matchs

### Rapports Disponibles
- Liste des joueurs par ordre alphabétique
- Liste des tournois
- Détails d'un tournoi spécifique
- Liste des joueurs d'un tournoi
- Détails des tours et matchs d'un tournoi

## Sauvegarde des Données

Toutes les données sont automatiquement sauvegardées dans des fichiers JSON dans le dossier `data/`. La synchronisation est automatique entre la mémoire et les fichiers.

## Conformité du Code

Le code suit les conventions PEP 8 avec une longueur de ligne maximale de 119 caractères. La conformité est vérifiée par flake8 et le rapport est disponible dans le dossier `flake8_rapport`.
