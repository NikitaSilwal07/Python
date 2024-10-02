#35. Write a Python program to replace every second character of a string with *.
user_input=input("Enter a string: ")
modify_string=""
for i in range(len(user_input)):
    if i==1:
        modify_string+="*"
    else:
        modify_string+=user_input[i]
print(modify_string)