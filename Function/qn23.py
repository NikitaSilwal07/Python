#23.Write a recursive function sum_digits(n) that returns the sum of the digits of a number.

def sum_digits(n):
    if n==0:
     return 0
    else:
      return n+sum_digits(n-1)

user_input=int(input("Enter the number"))
print(f"The sum of digits of a number{user_input} is {sum_digits(user_input)}")