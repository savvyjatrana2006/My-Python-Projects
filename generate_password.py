import random
import string

def generate_password(length, complexity):
    # Define character sets for different complexity levels
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Based on complexity, create the pool of characters to choose from
    if complexity == 1:
        char_pool = lowercase_letters
    elif complexity == 2:
        char_pool = lowercase_letters + uppercase_letters
    elif complexity == 3:
        char_pool = lowercase_letters + uppercase_letters + digits
    elif complexity == 4:
        char_pool = lowercase_letters + uppercase_letters + digits + symbols
    else:
        raise ValueError("Invalid complexity level! Choose between 1 and 4.")

    # Generate a random password from the character pool
    password = ''.join(random.choice(char_pool) for _ in range(length))

    return password

# Main function to get user inputs
def main():
    print("Welcome to the Password Generator!")

    # Get the desired length of the password
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a valid positive number.")
            return
    except ValueError:
        print("Please enter a valid number!")
        return
    
    # Get the complexity level from the user
    print("""
    Choose the complexity level:
    1. Lowercase letters only
    2. Lowercase and uppercase letters
    3. Lowercase, uppercase letters, and digits
    4. Lowercase, uppercase letters, digits, and symbols
    """)
    
    try:
        complexity = int(input("Enter the complexity level (1-4): "))
        if complexity < 1 or complexity > 4:
            print("Please choose a valid complexity level between 1 and 4.")
            return
    except ValueError:
        print("Please enter a valid number!")
        return
    
    # Generate and print the password
    password = generate_password(length, complexity)
    print(f"Your generated password is: {password}")

# Run the password generator
if __name__ == "__main__":
    main()

