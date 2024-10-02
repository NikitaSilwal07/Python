# 25. Write a Python program to convert a string from snake_case to camelCase.

user_input=input("Enter a snake_string: ")
words=user_input.split("_")
joined_word=words[0]+"".join(word.capitalize() for word in words[1::])
print(f"camelCase is: {joined_word}")