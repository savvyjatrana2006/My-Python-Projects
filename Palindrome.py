import re

def isPalindrome(s: str) -> bool:
    # Remove all non-alphanumeric characters and convert the string to lowercase
    cleaned_string = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

# Prompt user for input and check if it's a palindrome
user_input = input("Enter a string: ")
result = isPalindrome(user_input)

# Output the result
print(f"Is the string '{user_input}' a palindrome? {result}")
