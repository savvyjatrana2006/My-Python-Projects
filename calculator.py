def calculate(expression: str) -> int:
    def evaluate(tokens):
        stack = []
        num = 0
        sign = "+"
        
        while tokens:
            char = tokens.pop(0)
            
            if char.isdigit():
                num = num * 10 + int(char)
                
            if char == "(":
                num = evaluate(tokens)
            
            if char in "+-*/)" or not tokens:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))  # Truncate towards zero
                
                num = 0
                sign = char
            
            if char == ")":
                break
        
        return sum(stack)
    
    # Preprocess the expression to remove spaces and handle it as a list of characters
    tokens = list(expression.replace(" ", ""))
    return evaluate(tokens)

# Sample test
expression = "3+2*2"
print(calculate(expression))  # Output: 7
