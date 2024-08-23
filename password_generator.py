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
