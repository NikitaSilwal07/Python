# 30. Write a Python program that checks if a string starts and ends with the same character.

user_input=input("Enter a string: ")
if user_input[0]==user_input[-1]:
    print(f"{user_input} starts and ends with same character.")
else:
    print(f"{user_input} does not starts and ends with same character.")