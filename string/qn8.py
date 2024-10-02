#Check if a given string is a palindrome (reads the same 
# backward as forward).

user_input=input("Enter a string: ")
if(user_input==user_input[::-1]):
    print(f"{user_input} is palindrome.")
else:
    print(f"{user_input} is not palindrome.")
