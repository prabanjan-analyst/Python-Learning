# Functions

def greet():
    print("Hello Everyone!")


greet()

# Parameters and Arguements


def greeting(name):
    print(f"Hello Mr.{name.title()}")


greeting("prabanjan")

# Keyword Arguements


def welcome_note(first_name, last_name):
    print(f"Welcome {first_name.title()} {last_name}")


welcome_note(last_name="kumar", first_name="praveen")

# Return


def sum(a, b):
    return a+b


result = sum(5, 7)
print(result)


# Default Arguements

def welcome_greet(name="guest"):
    print(f"Welcome {name.title()}")


welcome_greet()
