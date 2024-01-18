import random

# Points de vie de l'ennemi et du joueur
ENNEMY_HEALTH = 50
PLAYER_HEALTH = 50

# Nombre de potions disponibles pour le joueur
NUMBER_OF_POTIONS = 3

# Variable pour gérer le tour passé du joueur
SKIP_TURN = False

# Boucle principale du jeu
while True:
    # Le jeu du joueur
    if SKIP_TURN:
        print("Vous passez votre tour...")
        SKIP_TURN = False  
    else:
        # Demander au joueur de choisir entre attaquer (1) ou utiliser une potion (2)
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")
        
        # Attaque
        if user_choice == "1":
            # Générer des dégâts aléatoires entre 5 et 15
            votre_attack = random.randint(5, 15)
            ENNEMY_HEALTH -= votre_attack
            print(f"Vous avez infligé {votre_attack} points de dégâts à l'ennemi") 
        # Potion
        elif user_choice == "2":
            if NUMBER_OF_POTIONS > 0:
                # Générer des points de vie aléatoires pour la potion entre 15 et 50
                potion_health = random.randint(15, 50)
                PLAYER_HEALTH += potion_health
                NUMBER_OF_POTIONS -= 1
                SKIP_TURN = True
                print(f"Vous récupérez {potion_health} points de vie ({NUMBER_OF_POTIONS} restantes)")
            else:
                print("Vous n'avez plus de potions...")
                continue
            
    # Vérifier si l'ennemi n'a plus de points de vie
    if ENNEMY_HEALTH <= 0:
        print("Vous avez gagné")
        break
    
    # Attaque de l'ennemi
    ennemy_attack = random.randint(5, 15)
    PLAYER_HEALTH -= ennemy_attack
    print(f"L'ennemi vous a infligé {ennemy_attack} points de dégâts")
    
    # Vérifier si le joueur n'a plus de points de vie
    if PLAYER_HEALTH <= 0:
        print("Tu as perdu")
        break
    
    # Afficher les statistiques
    print(f"Il vous reste {PLAYER_HEALTH} points de vie.")
    print(f"Il reste {ENNEMY_HEALTH} points de vie à l'ennemi.")
    print("-" * 50)
    
# Message de fin du jeu
print("Fin du jeu.")
