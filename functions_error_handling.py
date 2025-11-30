"""Functions for error handling for users input"""

def get_int_input(prompt, min_value=None, max_value=None):#error handling for user input for numbers
    while True:                    #Loop until the user gives valid input
        try:
            value = int(input(prompt))   # Try converting input to a number
            if min_value is not None and value < min_value or value > max_value:
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print(f"Invalid input. Please enter a number between {min_value} and {max_value}.")

def get_choice(prompt, valid_choices):#error handling for user input for letters
    valid_choices = [c.upper() for c in valid_choices]
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter one of these {valid_choices}")