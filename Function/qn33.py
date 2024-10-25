#33.Write a lambda function to check if a given string is a palindrome.

string="Nikita"
reverse_string=lambda string:string[::-1]
if reverse_string(string)==string:
 print(f"{string} is palindrome.")
else:
 print(f"{string} is not palindrome.")