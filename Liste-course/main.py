import sys

# Déclaration d'une liste vide pour stocker les éléments
LISTE = []

# Définition du menu avec les options
MENU = """Choisissez parmi les 5 options : 
1 : Ajouter un élément à la liste
2 : Retirer un élément de la liste
3 : Afficher la liste
4 : Vider la liste
5 : Quitter
Votre choix :"""

# Liste des choix valides du menu
MENU_CHOICES = ["1", "2", "3", "4", "5"]

# Boucle principale pour l'interaction avec l'utilisateur
while True:
    user_choice = ""
    
    # Boucle pour demander à l'utilisateur de choisir une option valide
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")
    
    # Option 1 : Ajouter un élément à la liste
    if user_choice == "1":
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")

    # Option 2 : Retirer un élément de la liste
    elif user_choice == "2":
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")

    # Option 3 : Afficher la liste
    elif user_choice == "3":
        if LISTE:
            print("Voici le contenu de votre liste :")
            # Boucle pour afficher les éléments de la liste avec leur position
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
                
        else:
            print("Votre liste ne contient aucun élément.")

    # Option 4 : Vider la liste
    elif user_choice == "4":
        LISTE.clear()
        print("La liste a été vidée de son contenu.")

    # Option 5 : Quitter le programme
    elif user_choice == "5":
        print("À bientôt !")
        sys.exit()

    # Affichage d'une ligne de 50 tirets pour séparer visuellement les étapes dans la console
    print("-" * 50)

