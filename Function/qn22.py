#22.Write a recursive function fibonacci_recursive(n) to return the n-th Fibonacci number.

def fibonacci_recursive(n):
    if n==0:
        result=0
    elif n==1:
       return 1
    else:
        result=fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
    return result

a=21
print(f"The {a} th fibonacci number is: {fibonacci_recursive(a)}")