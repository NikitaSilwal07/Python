#15.Write a function find_gcd(a, b) that returns the greatest common divisor of two numbers.

def find_gcd(a,b):
    gcd=b if a>b else a
    while True:
        if a%gcd ==0 and b%gcd==0:
          return gcd
        else:
          gcd-=1
a=88
b=66
print("The greatest common divisior of a and b is",find_gcd(a,b))
#or
print(f"The greatest common divisor of {a} and {b} is {find_gcd(a,b)}.")