def calculer_variation(premier_taux, dernier_taux):
    """Calcule la variation en pourcentage entre deux taux."""
    if premier_taux == 0:
        return 0
    return ((dernier_taux - premier_taux) / premier_taux) * 100

def calculer_moyenne(liste_taux):
    """Calcule la moyenne d'une liste de taux."""
    if not liste_taux:
        return 0
    return sum(liste_taux) / len(liste_taux)