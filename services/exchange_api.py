import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import pandas as pd
from datetime import date, timedelta
from database.repository import save_taux_data 

fin = date.today()
debut = fin - timedelta(days=30)

devises = "USD,GBP,JPY,CHF"
url = f"https://api.frankfurter.app/{debut}..{fin}?from=EUR&to={devises}"

reponse = requests.get(url)

if reponse.status_code == 200:
    donnees = reponse.json()
    
    lignes = []
    for jour, taux_jour in donnees['rates'].items():
        for nom_devise, valeur in taux_jour.items():
            lignes.append({
                "date": jour, 
                "devise": nom_devise, 
                "taux": valeur
            })
            
    df = pd.DataFrame(lignes)
    save_taux_data(df)
    
    print("Données enregistrées dans SQLite avec succès !")
    print(df.head())
else:
    print("Erreur API. Code :", reponse.status_code)