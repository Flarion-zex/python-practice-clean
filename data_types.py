# ================================
# PYTHON DATA TYPES EXAMPLES 
# ================================

# 1. Integer
a = 10
print("Integer: ",a , type(a))

# 2. Float
b = 10.5
print("Float : ", b, type(b))

# 3. String
c = "Hello Python"
print("String : ", c, type(c))

# 4. Boolean
d = True
print("Boolean : ", d, type(d))

# 5. List (mutable)
e = [1, 4, 7, 9]
print("List : ", e, type(e))

# 6. Tuple (immutable)
f = (6, 8, 9)
print("Tuple : ", f, type(f))

# 7. Dictonary (key-value pairs)
g = {"name" : "Ankit", "age" : 20}
print("Dictonary: ", g, type(g))

# 8. Set (unique value)
h = {1, 2, 3, 4}
print("Set : ", h, type(h))

# 9. None Type
i = None
print("NoneType : ", i, type(i))

# 10. complex number
j = 2 + 4j
print("Complex : ", j, type(j))


# ===========================
# PRACTICE EXAMPLES
# ===========================

# change data type using typecasting

x = "100"
y = int(x)
print("\nConverted String to Int : ", y, type(y))

# Boolean check

print("Bool from 0 :", bool(0))
print("Bool from 5 :", bool(5))

# Final message 
print("\nData Types Practice Completed ✅")