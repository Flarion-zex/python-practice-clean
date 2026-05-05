# =====================================
# LISTS IN PYTHON 
# =====================================

# 1. Creating a list
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)


# 2. Accessing elements (indexing)
print("First element:", numbers[0])
print("Last element:", numbers[-1])


# 3. List slicing
print("First 3 elements:", numbers[0:3])
print("Last 2 elements:", numbers[-2:])
print("Reversed list:", numbers[::-1])


# ==============================
# List Methods
# ==============================

# Append (add element at end)
numbers.append(60)
print("\nAfter append:", numbers)

# Insert (add at specific position)
numbers.insert(1, 15)
print("After insert:", numbers)

# Remove (remove specific value)
numbers.remove(30)
print("After remove:", numbers)

# Pop (remove last element)
numbers.pop()
print("After pop:", numbers)

# Sort list
numbers.sort()
print("Sorted list:", numbers)

# Reverse list
numbers.reverse()
print("Reversed order:", numbers)


# ==============================
# Other Useful Functions
# ==============================

print("\nLength:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


# ==============================
# Loop through list
# ==============================

print("\nLoop through list:")
for num in numbers:
    print(num)


# ==============================
# PRACTICE EXAMPLE
# ==============================

# Taking input list from user
user_list = []

n = int(input("\nHow many elements you want to add? "))

for i in range(n):
    val = int(input("Enter number: "))
    user_list.append(val)

print("Your list:", user_list)
print("Sorted:", sorted(user_list))


# Final message
print("\nList Practice Completed ✅")
