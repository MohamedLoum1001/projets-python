# Les compréhensions de liste en python
nbres = [1, 21, 5, 6, 24, 7, 73, 25, 48]
# Ajouter tous les nombres pairs dans le tableaux nbres_pairs
nbres_pairs = [i for i in nbres if i % 2 == 0]
print(nbres_pairs)
print()
print("Ajouter tous les nombres positifs dans le tableaux nbres_positifs")
nbres = range(-10, 10)
# Ajouter tous les nombres positifs dans le tableaux nbres_positifs
nbres_positifs = [i for i in nbres if i >= 0]
print(nbres_positifs)
print()

print("Doubler tous les nombres  et les ajouter dans le tableaux nbres_doubles")
nbres = range(5)
# Doubler tous les nombres  et les ajouter dans le tableaux nbres_doubles
nbres_doubles = [i * 2 for i in nbres]
print(nbres_doubles)
print()

nbres = range(10)
nbres_inverses = [i if i % 2 == 0 else -i for i in nbres]
print(nbres_inverses)
print()
# for i in range(10):
#     print(f"Utilisateur {i+1}")
# for i in range(1, 11):
#     print(f"Utilisateur", i)

i = 1
while i < 11:
    print("Utilisateur ", i)
    i +=1

# Inverser les mots 
mot = input("Entrez un prénom : ")
# la fonction (list) nous permet de convertir un objet en liste
# print(list(reversed(mot)))
for letter in reversed(mot):
    print(letter)

# Boucle while
continuer = 'o'
while continuer == 'o':
    print("On continue...")
    continuer = input("Voulez-vous continuer ? o/n : ")
    # if resultat != "o":
    #     break