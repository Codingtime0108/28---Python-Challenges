import random
import string
def generate_password():
    lowercase_letters = "abcdefghhijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    password = random.choice(lowercase_letters)+ random.choice(uppercase_letters)+ random.choice(digits)+ random.choice(lowercase_letters)+ random.choice(uppercase_letters)+ random.choice(digits)
    
    if len(password)> 6:
        print("Password length should be at least 6 digits for security.")
        return None
    print(password)
generate_password()