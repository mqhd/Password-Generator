import random
import string
import pyperclip

def generate_password(length=12, use_punctuation=True):
    characters = string.ascii_letters + string.digits
    if use_punctuation:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    print("==================")
    length = int(input("Enter the length of the password: "))
    include_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
    password = generate_password(length, include_punctuation)
    print("Generated Password:", password)
    
    # Copy the password to the clipboard
    pyperclip.copy(password)
    print("Password copied to clipboard.")

if __name__ == "__main__":
    main()

# Copyright Mohammad Fahad Altamimi
