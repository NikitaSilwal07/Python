#5. Write a function reverse_string(s) that returns the reverse of the input string s.

def reverse_string(s): 
   return s[::-1] 
user_input=input("Enter a string : ") 
print(f"The reverse of {user_input} is : {reverse_string(user_input)}") 