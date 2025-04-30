# For Loop

# for number in range(1, 4):
#     print(f"Attempt {number}")


send_successfull = False
for number in range(1, 4):
    print(f"Attempt {number}")
    if send_successfull:
        print("Message send Successfully...")
        break
else:
    print("Failed to send message")


# Nested Loops

for x in range(1, 4):
    for y in range(1, 3):
        print(f"({x}, {y})")


# Iterable
for x in "Prabanjan":
    print(x)

shopping_cart = ["Mobile", "Grocery", "Laptop", "Home Decors"]
for item in shopping_cart:
    print(f"You ordered {item} from Amazon")


for item in shopping_cart:
    if len(item) <= 6:
        print(item.upper())


# While Loops
command = ""

while command != "quit":
    print("Enter quit to QUIT")
    command = input("> ").lower()
    if command == "quit":
        print("Exiting...")
    else:
        print(f"Your command: {command}")
