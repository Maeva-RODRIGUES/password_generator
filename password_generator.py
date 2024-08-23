# password_generator.py
#print("Hello, world!")
  
#Importation des bibliothèques
import random  # Importation du module random pour générer des choix aléatoires
import string  # Importation du module string pour accéder aux ensembles de caractères prédéfinis

# Fonction pour générer un mot de passe avec les options de personnalisation
def generate_password(length, use_uppercase=True, use_digits=True, use_punctuation=True):
    characters = string.ascii_lowercase  # Commence avec les lettres minuscules
    if use_uppercase:  # Ajoute les majuscules si l'utilisateur l'a demandé
        characters += string.ascii_uppercase
    if use_digits:  # Ajoute les chiffres si l'utilisateur l'a demandé
        characters += string.digits
    if use_punctuation:  # Ajoute les caractères spéciaux si l'utilisateur l'a demandé
        characters += string.punctuation

    # Vérifie que le jeu de caractères n'est pas vide
    if not characters:
        raise ValueError("Aucune catégorie de caractères sélectionnée pour générer le mot de passe.")

    # Génère le mot de passe en choisissant des caractères aléatoires parmi ceux sélectionnés
    password = ''.join(random.choice(characters) for i in range(length))
    return password  # Retourne le mot de passe généré

# Fonction principale pour exécuter le script
def main():
    print("Bienvenue dans le générateur de mot de passe !")  # Message de bienvenue pour l'utilisateur
    
    # Boucle pour demander une longueur de mot de passe valide
    while True:
        try:
            length = int(input("Entrez la longueur du mot de passe : "))  # Demande la longueur du mot de passe
            if length <= 0:  # Vérifie que la longueur est positive
                print("La longueur doit être un entier positif.")
            else:
                break  # Sort de la boucle si l'entrée est valide
        except ValueError:  # Gère les cas où l'entrée n'est pas un entier
            print("Veuillez entrer un nombre entier valide.")

    # Demande à l'utilisateur s'il veut inclure des majuscules
    use_uppercase = input("Inclure des lettres majuscules ? (oui/non) : ").lower() in ['oui', 'o', 'yes', 'y', '']
    
    # Demande à l'utilisateur s'il veut inclure des chiffres
    use_digits = input("Inclure des chiffres ? (oui/non) : ").lower() in ['oui', 'o', 'yes', 'y', '']
    
    # Demande à l'utilisateur s'il veut inclure des caractères spéciaux
    use_punctuation = input("Inclure des caractères spéciaux ? (oui/non) : ").lower() in ['oui', 'o', 'yes', 'y', '']

    # Essaye de générer le mot de passe avec les paramètres spécifiés
    try:
        password = generate_password(length, use_uppercase, use_digits, use_punctuation)
        print(f"Votre mot de passe généré est : {password}")  # Affiche le mot de passe généré
    except ValueError as e:  # Gère l'erreur si aucune catégorie de caractères n'est sélectionnée
        print(e)

    # Point d'entrée du script, exécute la fonction main si le script est lancé directement
    if __name__ == "__main__":
        main()
