students = ["Prabanjan", "Thirupathy", "Prasanth", "Rajkumar"]

print(students)
print(students[2])      # Access the Elements using index
print(students[-2])     # Range of the list is the last range will exclusive
print(students[1:3])

for student in students:
    print(student.upper())


numbers = [4, 5, 7, 1, 2, 9, 6, 12]

# to find the largest number in the list
large_num = numbers[0]
for number in numbers:
    if number > large_num:
        large_num = number
print(number)


# 2D lists
matrix = [
    [1, 2, 3],
    [3, 2, 1],
    [4, 5, 6]
]

print(matrix)
print(matrix[1])
print(matrix[1][1])

# List methods
nums = [1, 2, 3, 4, 5, 6]

nums.append(4)      # Add at End

print(nums.count(4))    # count the same value
nums.insert(1, 10)      # insert the value with index
nums.pop()              # Removes the Last value
nums.remove(10)         # Removes the exact value
nums.sort()             # Accending order
nums.reverse()          # Decending order
nums2 = nums.copy()     # Take a copy of the original
print(nums2)

nums.clear()            # Remove all the values
print(nums)


# Find the Unique numbers

numbers2 = [2, 3, 2, 6, 7, 4, 3, 1, 9, 2]

unique_nums = []

for num in numbers2:
    if num not in unique_nums:
        unique_nums.append(num)
print(unique_nums)
