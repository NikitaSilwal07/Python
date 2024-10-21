#6. Write a function is_palindrome(s) that checks if the input string s is a palindrome.

def is_palindrome(s): 
    if s==s[::-1]: 
      return True 
    else: 
      return False 
    
user_input=input("Enter a string : ")  
if is_palindrome(user_input): 
    print(f"{user_input} is palindrome.") 
else: 
    print(f"{user_input} is not palindrome.") 