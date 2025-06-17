import random

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    """
    Genere un mot de passe aleatoire en fonction des options choisies.
    param length: Longueur du mot de passe
    param include_uppercase: Inclure des lettres majuscules
    param include_lowercase: Inclure des lettres minuscules
    param include_numbers: Inclure des chiffres
    param include_symbols: Inclure des symboles
    return: Mot de passe genere
    """
    characters = ""
    
    if include_uppercase:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_lowercase:
        characters += "abcdefghijklmnopqrstuvwxyz"
    if include_numbers:
        characters += "0123456789"
    if include_symbols:
        characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    if not characters:
        return "Please select at least one character type."
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        return password