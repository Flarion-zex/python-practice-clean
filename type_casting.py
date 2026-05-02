# =====================================
# TYPE CASTING PRACTICE 
# =====================================

# 1. String to Integer
num_str = "25"
num_int = int(num_str)
print("String to Int:", num_int, type(num_int))


# 2. String to Float
float_str = "45.67"
num_float = float(float_str)
print("String to Float:", num_float, type(num_float))


# 3. Integer to Float
a = 10
b = float(a)
print("Int to Float:", b, type(b))


# 4. Float to Integer
price = 99.99
price_int = int(price)
print("Float to Int:", price_int, type(price_int))


# 5. Integer to String
x = 100
x_str = str(x)
print("Int to String:", x_str, type(x_str))


# 6. Float to String
y = 55.5
y_str = str(y)
print("Float to String:", y_str, type(y_str))


# 7. Boolean Conversion
print("Bool from 0:", bool(0))
print("Bool from 1:", bool(1))
print("Bool from empty string:", bool(""))
print("Bool from text:", bool("Python"))


# 8. List to Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("List to Tuple:", my_tuple, type(my_tuple))


# 9. Tuple to List
t = (4, 5, 6)
l = list(t)
print("Tuple to List:", l, type(l))


# 10. Set to List
s = {7, 8, 9}
list_from_set = list(s)
print("Set to List:", list_from_set, type(list_from_set))


# ==============================
# PRACTICE EXAMPLE
# ==============================

# Taking input and converting to integer
user_input = input("\nEnter a number: ")
converted = int(user_input)
print("After conversion:", converted, type(converted))


# ==============================
# ERROR EXAMPLE (COMMENTED)
# ==============================

# text = "hello"
# print(int(text))  # ❌ This will give error


print("\nType Casting Practice Completed ✅")