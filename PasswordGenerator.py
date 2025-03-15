import string
import random

# Get password length from the user
length = int(input("Enter the desired password length: "))

print("Select the character types to include in your password:")
print("1. Letters (A-Z, a-z)")
print("2. Digits (0-9)")
print("3. Special Characters (!@#$%^&* etc.)")
print("4. Done (Generate Password)")

char_pool = ""

# Loop to allow multiple selections
while True:
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("Letters added to the password.")
        char_pool += string.ascii_letters
    elif choice == "2":
        print("Digits added to the password.")
        char_pool += string.digits
    elif choice == "3":
        print("Special characters added to the password.")
        char_pool += string.punctuation
    elif choice == "4":
        if char_pool:  # Ensure at least one type of character is selected
            break
        else:
            print("You must select at least one character type before proceeding.")
    else:
        print("Invalid option, please choose between 1-4.")

# Generate the password
password = "".join(random.choices(char_pool, k=length))

print("\nYour randomly generated password: ", password)
