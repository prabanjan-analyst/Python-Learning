# Comparison operators
print(10 > 5)       # Greater than
print(10 < 5)       # Less than
print(10 >= 5)      # Greater than or equal to
print(10 <= 5)      # Less than or equal to
print(10 == 5)      # Equal to
print(10 == "10")   # Equal to
print(10 != "10")   # Not equal to

# Conditional Statements
# If Statements

temp = 35

if temp > 30:
    print("Its Hot Drink more water!")
else:
    print("Stay cool!")


if temp < 30:
    print("Its Cold")
elif temp > 30:
    print("Its very Hot!")
else:
    print("Stay inside!")


student_mark = int(input("Enter Your mark: "))
if student_mark <= 35:
    print(f"You got below 35 marks")
    print("You Fail")
else:
    print(f"You got above 35 marks")
    print("You Pass")


# Ternary Operator
age = 18

if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

# print(message)

message1 = "Eligible" if age >= 18 else "Not Eligible"
# print(message1)


# Logical Operators AND OR NOT
is_employee = True
permanent_emp = True
promoted = False

# if is_employee:
#     print("Prabanjan is our company Employee...")
# else:
#     print("Invalid Data")


if is_employee and permanent_emp:
    print("Prabanjan is our company permanent Employee.")
else:
    print("Invalid Data")

if not is_employee:
    print("He is not our Employee")
else:
    print("Invalid data")

# Short circuit operator
if is_employee or permanent_emp and promoted:
    print("True...")
else:
    print("False...")
