#36.Write a function multiply_all(*args) that multiplies all the numbers passed as arguments.

def multiply_all(*args):
 product=1
 for x in args:
      product*=x
 return product
print("The sum of 2,3,4,5,6 is: ",multiply_all(2,3,4,5,6))