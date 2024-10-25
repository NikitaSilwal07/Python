#26.Write a recursive function power(x, n) that returns x raised to the power of n.

def power(x,n):
    if n==1:
      return x
    else:
       return x*power(x,n-1)
a=6
n=3
print(f'{a} power {n} is : {power(a,n)}')