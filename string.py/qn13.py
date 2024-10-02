# 13. Write a program to compare two strings lexicographically and determine which one
#  comes first alphabetically.

user_input1=input("Enter a string1: ")
user_input2=input("Enter a string2: ")
if user_input1<user_input2:
    print(f'{user_input1} comes before {user_input2}.')
elif user_input2<user_input1:
    print(f'{user_input2} comes before {user_input1}.')
else:
    print(f'{user_input1} and {user_input2} are same.')