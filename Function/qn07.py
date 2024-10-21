#7. Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence.

def fibonacci(n): 
    first_number=0 
    second_number=1 
    fibonacci_series=[first_number,second_number] 
    for i in range(2,n): 
        temp=first_number 
        first_number=second_number 
        second_number=first_number+temp 
        fibonacci_series.append(second_number) 
    return fibonacci_series 
 
user_input=int(input("Enter a number to find to number of fibonacci sequence : ")) 
print(f"The fibonacci sequence upto {user_input} term is: {fibonacci(user_input)}") 