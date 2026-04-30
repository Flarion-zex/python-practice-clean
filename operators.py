# ================================
# PYTHON OPERATORS PRACTICE
# ================================

# 1. Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print("\n---------------------\n")

# 2. Comparison Operators
x = 5
y = 10

print("Comparison Operators:")
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater:", x > y)
print("Less:", x < y)
print("Greater or Equal:", x >= y)
print("Less or Equal:", x <= y)

print("\n---------------------\n")

# 3. Logical Operators
p = True
q = False

print("Logical Operators:")
print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)

print("\n---------------------\n")

# 4. Assignment Operators
num = 10

print("Assignment Operators:")
num += 5
print("+= :", num)

num -= 3
print("-= :", num)

num *= 2
print("*= :", num)

num /= 4
print("/= :", num)

print("\n---------------------\n")

# 5. Bitwise Operators
m = 5   # 0101
n = 3   # 0011

print("Bitwise Operators:")
print("AND:", m & n)
print("OR:", m | n)
print("XOR:", m ^ n)
print("NOT:", ~m)
print("Left Shift:", m << 1)
print("Right Shift:", m >> 1)

print("\n---------------------\n")

# 6. Membership Operators
list1 = [1, 2, 3, 4]

print("Membership Operators:")
print("2 in list:", 2 in list1)
print("5 not in list:", 5 not in list1)

print("\n---------------------\n")

# 7. Identity Operators
a = [1, 2]
b = [1, 2]
c = a

print("Identity Operators:")
print("a is b:", a is b)
print("a is c:", a is c)
print("a is not b:", a is not b)