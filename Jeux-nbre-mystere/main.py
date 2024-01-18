from random import randint

# Générer un nombre mystère aléatoire entre 0 et 50 inclus
nbre_to_find = randint(0, 50)

# Nombre d'essais restants pour l'utilisateur
remaining_attempts = 5

print("*** Le jeu du nombre mystère ***")

# Boucle principale
while remaining_attempts > 0:
    # Afficher le nombre d'essais restants à l'utilisateur
    print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

    # Saisie de l'utilisateur
    user_choice = input("Devine le nombre : ")

    # Vérifier si l'entrée de l'utilisateur est un nombre
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue
    
    user_choice = int(user_choice)

    # Comparer le nombre mystère avec celui choisi par l'utilisateur
    # et donner des indices sur la relation entre les deux
    if nbre_to_find > user_choice:
        print(f"Le nombre mystère est plus grand que {user_choice}")
    elif nbre_to_find < user_choice:
        print(f"Le nombre mystère est plus petit que {user_choice}")
    else:
        # L'utilisateur a deviné correctement, sortir de la boucle
        break
        
    # Réduire le nombre d'essais restants
    remaining_attempts -= 1

# Gagné ou perdu
if remaining_attempts == 0:
    print(f"Dommage ! Le nombre mystère était {nbre_to_find} !")
else:
    print(f"Bravo ! Le nombre mystère était bien {nbre_to_find} !")
    # Calculer le nombre d'essais réussis en soustrayant le nombre d'essais restants initiaux
    print(f"Tu as trouvé le nombre mystère en {6 - remaining_attempts} essai(s)")

# Message de fin du jeu
print("Fin du Jeu.")
