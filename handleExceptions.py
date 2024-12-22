try:
    # Code qui peut provoquer une exception
    nombre = int(input("Entrez un nombre : "))
    résultat = 10 / nombre
except ValueError:
    # Gestion des erreurs de type (ex. entrer une chaîne au lieu d'un nombre)
    print("Erreur : Vous devez entrer un nombre valide.")
except ZeroDivisionError:
    # Gestion de la division par zéro
    print("Erreur : Division par zéro non autorisée.")
else:
    # S'exécute si aucune exception ne survient
    print(f"Résultat : {résultat}")
finally:
    # S'exécute dans tous les cas
    print("Fin du programme.")
