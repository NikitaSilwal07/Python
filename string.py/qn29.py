# 29. Write a program that takes a string and removes the first and last characters.

user_input=input("Enter a string: ")
user_input=user_input[1:len(user_input)-1:1]
print(user_input)