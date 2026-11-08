import sqlite3
import os

# Le nom du fichier de base de données qui sera créé
DB_PATH = "devise_track.db"

def get_connection():
    """Crée et retourne une connexion à la base de données SQLite."""
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    """Initialise la base de données et crée les tables si elles n'existent pas."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Création de la table pour l'historique des taux
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historique_taux (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            devise TEXT NOT NULL,
            taux REAL NOT NULL,
            UNIQUE(date, devise)
        )
    """)
    
    # Création de la table pour les alertes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alertes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            devise TEXT NOT NULL,
            seuil REAL NOT NULL,
            type_alerte TEXT NOT NULL, 
            est_declenchee INTEGER DEFAULT 0
        )
    """)
    
    conn.commit()
    conn.close()
    print("Base de données initialisée avec succès.")

if __name__ == "__main__":
    # Ce bloc s'exécute uniquement si on lance ce fichier directement
    init_db()