import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # a-z A-Z
    if use_digits:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # !@#$%^&* etc.

    if not characters:
        return "You must choose at least one character set."

    # Use random.choices to generate password
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("🔐 Welcome to Password Generator 🔐")
    
    # Get user input
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Character type preferences
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_symbols)
    print(f"\n🧾 Your generated password: {password}")

# Run the main function
if __name__ == "__main__":
    main()
