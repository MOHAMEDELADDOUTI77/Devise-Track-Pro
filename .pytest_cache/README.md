# DeviseTrack Pro

Application web interactive de suivi et d'analyse des taux de change. Ce projet a été développé pour illustrer des compétences en développement Python, manipulation de données et intégration d'API REST.

## Fonctionnalités

- **Données réelles** : Récupération des taux de change via l'API publique Frankfurter.
- **Tableau de bord interactif** : Sélection de la devise, affichage du taux actuel, de la moyenne sur 30 jours et de la variation.
- **Graphiques dynamiques** : Visualisation de l'évolution des taux avec Plotly.
- **Base de données** : Sauvegarde de l'historique des taux et des alertes dans une base SQLite.
- **Système d'alertes** : Création d'alertes personnalisées avec déclenchement visuel si le seuil est atteint.
- **Tests automatisés** : Vérification de la fiabilité des calculs avec Pytest.

## Technologies utilisées

- **Langage** : Python 3
- **Interface** : Streamlit
- **Data** : Pandas, Requests
- **Visualisation** : Plotly
- **Base de données** : SQLite (module natif `sqlite3`)
- **Tests** : Pytest
- **Versioning** : Git & GitHub

## Architecture du projet

```text
DeviseTrack-Pro/
│
├── app.py                        # Point d'entrée de l'application Streamlit
├── requirements.txt              # Dépendances du projet
├── .gitignore                    # Fichiers ignorés par Git
├── README.md                     # Documentation
│
├── config/                       # Fichiers de configuration
├── components/                   # Composants d'interface (si séparés)
│
├── database/                     # Gestion de la base de données
│   ├── connection.py             # Connexion SQLite
│   └── repository.py             # Requêtes SQL (CRUD)
│
├── services/                     # Logique métier
│   ├── exchange_api.py           # Appels à l'API
│   └── exchange_calculations.py  # Calculs (moyenne, variation)
│
└── tests/                        # Tests unitaires
    └── test_calculations.py      # Tests des fonctions de calcul