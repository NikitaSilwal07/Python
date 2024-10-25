#16.Write a function sum_of_squares(n) that returns the sum of squares of the first n natural numbers.

def sum_of_squares(n):
    sum=0
    for i in range(1,n+1):
        sum+=i**2
    return sum
user_input = int(input("Enter the number"))
print("The sum of squares of the first n natural number is",sum_of_squares(user_input))
