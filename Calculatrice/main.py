# Initialisation des variables a et b avec des chaînes vides
a = b = ""

# Utilisation d'une boucle while pour demander à l'utilisateur d'entrer deux nombres valides
while not (a.isdigit() and b.isdigit()):
    # Demander à l'utilisateur d'entrer un premier nombre
    a = input("Veuillez entrer un premier nombre : ")

    # Demander à l'utilisateur d'entrer un deuxième nombre
    b = input("Veuillez entrer un deuxième nombre : ")

    # Vérifier si les deux entrées sont des nombres valides en utilisant isdigit()
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")

# Afficher le résultat de l'addition des deux nombres
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
