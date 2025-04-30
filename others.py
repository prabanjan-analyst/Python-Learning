# Tuples

# It means we cant modify this immutable
numbers = (1, 2, 3)

# Unpacking
x = numbers[0]
y = numbers[1]
z = numbers[2]

print(x)
print(y)
print(z)

# but we use unpacking
a, b, c = numbers
print(a)
print(b)
print(c)

# Dictionaries

user = {
    "name": "Prabanjan",
    "age": 27,
    "is_employee": False
}

print(user)
print(user["name"])

user["age"] = 28
print(user["age"])

# Exceptions

# user_age = int(input("Enter your Age: "))
# print(user_age)     # In case we type the string it return ValueError

# In this situation we use try expect
try:
    user_age = int(input("Enter your Age: "))
    print(user_age)
except:      # We can also mention the exact error => except ValueError
    print("Invalid Number")
