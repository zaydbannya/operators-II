# Function to check if the input is an alphabet or a number
def check_input(char):
    if char.isalpha():
        return "It's an alphabet."
    elif char.isdigit():
        return "It's a number."
    else:
        return "It's neither an alphabet nor a number."

# Example usage
user_input = input("Enter a character: ")
result = check_input(user_input)
print(result)
