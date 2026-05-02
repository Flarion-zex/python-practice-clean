# =====================================
# STRING IN PYTHON
# =====================================

# 1. Creating strings
name = "Ankit"
language = 'Python'

print("Name:", name)
print("Language:", language)


# 2. String concatenation
greeting = "Hello " + name
print("Greeting:", greeting)


# 3. String indexing
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])


# 4. String slicing
print("Slice [0:3]:", text[0:3])
print("Reverse string:", text[::-1])


# 5. String methods
msg = "  hello python  "

print("Upper:", msg.upper())
print("Lower:", msg.lower())
print("Title:", msg.title())
print("Strip:", msg.strip())


# 6. Replace and find
sentence = "I love Java"
print("Replace:", sentence.replace("Java", "Python"))
print("Find 'love':", sentence.find("love"))


# 7. Checking string
print("Is alphabet:", name.isalpha())
print("Is digit:", "123".isdigit())


# 8. Length of string
print("Length:", len(name))


# 9. Taking input string
user_name = input("\nEnter your name: ")
print("Welcome", user_name)


# ==============================
# PRACTICE EXAMPLE
# ==============================

word = input("\nEnter a word: ")
print("Reversed word:", word[::-1])


# Final message
print("\nString Practice Completed ✅")