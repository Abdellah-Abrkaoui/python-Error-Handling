def verifier_age(age):
    if age < 18:
        # Lever une exception si l'age est inferieur a 18
        raise ValueError("Acces refuse : Vous devez avoir au moins 18 ans.")
    elif age > 120:
        # Lever une exception pour un age non raaliste
        raise ValueError("Erreur : L'age entre n'est pas valide.")
    else:
        print("Acces autorise. Bienvenue !")

try:
    utilisateur_age = int(input("Entrez votre age : "))
    verifier_age(utilisateur_age)
except ValueError as e:
    # Gerer l'exception et afficher le message d'erreur
    print(f"Erreur detectee : {e}")
finally:
    print("Fin de la verification.")
