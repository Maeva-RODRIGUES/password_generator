# password_generator.py
#print("Hello, world!")
  
#Importation des bibliothèques
import random
import string

# Fonction pour générer le mot de passe
def generate_password(length):
    # Vérifie que la longueur est positive
    if length <= 0:
        raise ValueError("La longueur du mot de passe doit être positive.")
    
    # Combinaison des caractères possibles
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Utilisation de random.choices pour générer le mot de passe
    password = ''.join(random.choices(characters, k=length))
    
    return password

# Fonction principale pour exécuter le script
def main():
    print("Bienvenue dans le générateur de mot de passe !")
    
    # Boucle jusqu'à ce que l'utilisateur entre une valeur correcte (capture les erreurs)
    while True:
        try:
            length = int(input("Entrez la longueur du mot de passe : "))
            if length <= 0:
                print("Veuillez entrer un nombre entier positif.")
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
    
    # Génération et affichage du mot de passe
    password = generate_password(length)
    print(f"Votre mot de passe généré est : {password}")

if __name__ == "__main__":
    main() #assure que le code soit exécuté diirectement et ,on importé comme module
