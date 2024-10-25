#25.Write a recursive function gcd_recursive(a, b) to find the greatest common divisor of two numbers.

def gcd_recursive(a,b):
    if b==0:
      return a
    else:
       return gcd_recursive(b , a%b)
a=23
b=12
print(f'The gcd of {a} and {b} is : {gcd_recursive(a,b)}') 