import secrets
import string

def generate_password(length=12):
    # Define character sets for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password using a secure random choice for each character
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Secure Password Generator!")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer for password length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get user input for the number of passwords to generate
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                print("Please enter a positive integer for the number of passwords.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate and display passwords
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        password = generate_password(length)
        print(password)

if __name__ == "__main__":
    main()
