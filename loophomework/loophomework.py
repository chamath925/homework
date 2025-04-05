def is_alphabet(char):
    if char.isalpha():
        return f"'{char}' is an alphabet."
    else:
        return f"'{char}' is not an alphabet."

# Get user input
char = input("Enter a character: ")

# Ensure only one character is entered
if len(char) == 1:
    print(is_alphabet(char))
else:
    print("Please enter only one character.")
