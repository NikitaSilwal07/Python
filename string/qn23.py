# 23. Write a Python program that checks if a string contains only alphabets (no digits or special characters).

user_input=input("Enter a string: ")
if(user_input.isalpha()):
    print("String contains only alphabet.")
else:
    print("String contains only other than alphabet.")