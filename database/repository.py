import sqlite3
import pandas as pd
from database.connection import get_connection

def save_taux_data(df):
    """Sauvegarde les données du DataFrame Pandas dans la base SQLite."""
    conn = get_connection()
    cursor = conn.cursor()
    
    for index, row in df.iterrows():
        cursor.execute("""
            INSERT OR IGNORE INTO historique_taux (date, devise, taux)
            VALUES (?, ?, ?)
        """, (row['date'], row['devise'], row['taux']))
        
    conn.commit()
    conn.close()
    print(f"{len(df)} lignes traitées pour la base de données.")

def get_taux_data():
    """Récupère toutes les données de la base et les retourne sous forme de DataFrame Pandas."""
    conn = get_connection()
    query = "SELECT date, devise, taux FROM historique_taux ORDER BY date ASC"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def ajouter_alerte(devise, seuil, type_alerte):
    """Enregistre une nouvelle alerte dans la base."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO alertes (devise, seuil, type_alerte, est_declenchee)
        VALUES (?, ?, ?, 0)
    """, (devise, seuil, type_alerte))
    conn.commit()
    conn.close()

def get_alertes_actives():
    """Récupère toutes les alertes qui n'ont pas encore été déclenchées."""
    conn = get_connection()
    query = "SELECT * FROM alertes WHERE est_declenchee = 0"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df