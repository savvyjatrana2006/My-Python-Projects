def isAllDigits(s: str) -> bool:
    return s.isdigit()

# Prompt user for input and check if all characters are digits
user_input = input("Enter a string: ")
result = isAllDigits(user_input)

# Output the result
print(f"Is the string '{user_input}' composed entirely of digits? {result}")
