while True:
    try:
        mdp = input("Entrez votre mot de passe (min 8 caractères) : ")

        if len(mdp) < 8:
            raise ValueError("Mot de passe trop court. Veuillez entrer un mot de passe d'au moins 8 caractères.")

        if len(mdp) == 0:
            raise ValueError("Mot de passe vide. Veuillez entrer un mot de passe.")

        if mdp.isdigit():
            raise ValueError("Le mot de passe ne doit pas contenir que des chiffres. Veuillez inclure des lettres et des caractères spéciaux.")

        print("Inscription terminée")
        break  # Sortir de la boucle si le mot de passe est valide

    except ValueError as ve:
        print(f"Erreur : {ve}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
    finally:
        print("Fin de l'itération.")
