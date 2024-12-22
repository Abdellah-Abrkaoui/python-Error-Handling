def diviser(a, b):
    if b == 0:
        raise ValueError("La division par zéro n'est pas permise.")
    return a / b

# Exemple d'utilisation
try:
    resultat = diviser(10, 0)
except ValueError as e:
    print(f"Erreur : {e}")
