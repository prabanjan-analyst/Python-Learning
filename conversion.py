x = "10"
print(type(x))

a = 20
b = str(a)
print(type(b))

# print(10 + b)     # It return Error bcoz b is String Dtype

y = int(x)
print(type(y))

z = bool(x)
print(type(z))
print(z)

# Falsy values return False
# 0, "", None are Falsy values
# -4 negative values also considered as True values

# Getting input from user
user_input = input("x: ")

print(f"You typed x as {user_input}")

# we can perform math operations
user_input2 = int(input("x: "))
print(
    f"Increased by 10 and you enter {user_input2}, The ans is: {user_input2 + 10}")
