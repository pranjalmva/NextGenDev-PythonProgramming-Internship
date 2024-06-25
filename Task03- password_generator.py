import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    length = int(input("Enter the desired length of the password: "))

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_special_chars = input("Include special characters? (y/n): ").lower() == "y"

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)

    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()