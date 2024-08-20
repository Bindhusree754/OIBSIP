import random
import string
import argparse

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Base character set
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Ensure at least one character type is included
    if not characters:
        raise ValueError("At least one character type must be included")
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a random password based on user-defined criteria.")
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password (default: 12)')
    parser.add_argument('--no-uppercase', action='store_false', help='Exclude uppercase letters')
    parser.add_argument('--no-numbers', action='store_false', help='Exclude numbers')
    parser.add_argument('--no-symbols', action='store_false', help='Exclude symbols')
    
    args = parser.parse_args()

    try:
        # Generate password
        password = generate_password(args.length, 
                                     use_uppercase=not args.no_uppercase,
                                     use_numbers=not args.no_numbers,
                                     use_symbols=not args.no_symbols)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
