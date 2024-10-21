#2. Write a function is_even(n) that returns True if a number is even, and False otherwise.

def is_even(num):
    if num%2==0:
       return True
    else:
       return False
       
a=25 
if is_even(a): 
    print(f"{a} is even.") 
else: 
    print(f"{a} is not even.") 