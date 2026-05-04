# =================================
# MINI PROJECT - USER INFO SYSTEM
# =================================

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# Processing data
is_adult = age >= 18

# Display output
print("\n===== USER INFORMATION ========")
print("Name:",name)
print("Age:", age)
print("City:", city)

# Conditional output
if is_adult:
    print("\nStatus: Adult")
else:
    print("\nStatus: minor")

# Additional feature : greeting
print("\nHello",name + "! Welcome from", city)


# ============================
# EXTRA PRACTICE FEATURE
# ============================

# Calculate birth year (approx)
current_year = 2026
birth_year = current_year - age

print("Estimated Birth Year :", birth_year)



# Final message
print("\nProgram completed successfully ✅")