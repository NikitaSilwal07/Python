#34. Write a program that checks if a string contains any numeric characters.
user_input=input("Enter a string: ")
for char in user_input:
    if char.isdigit()==True:
        print(f"{user_input} contains some numeric.")
        break
    else:
        continue
else:
    print(f"{user_input} does not contain any string.")