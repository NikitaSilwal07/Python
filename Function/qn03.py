#3. Write a function factorial(n) that returns the factorial of a given number n.

def fact(num):
    result=1
    while num>1:
      result = result * num
      num= num -1
    return result

print(fact(5))
#0r
a=fact(5)
print(a)
