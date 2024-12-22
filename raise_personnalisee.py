class MonException(Exception):
    pass

def verifier_positif(nombre):
    if nombre < 0:
        raise MonException("Le nombre doit être positif.")
    return nombre

# Exemple d'utilisation
try:
    verifier_positif(-5)
except MonException as e:
    print(f"Erreur  : {e}")
