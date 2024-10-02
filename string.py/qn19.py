# 19. Write a program to remove duplicate characters from a string while preserving the order of characters.

input_string = "Python is fun."
result = []
seen = []
for char in input_string:
    if char not in seen:
        result.append(char)
        seen.append(char)
print("Original string:", input_string)
print("String without duplicates:", "".join(result))