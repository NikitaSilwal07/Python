#35.Write a function sum_all(*args) that takes any number of arguments and returns their sum.

def sum_all(*args):
 sum=0
 for x in args:
    sum+=x
 return sum
print("The sum of 1,2,3,4,6,7,8,9,11,12 is: ",sum_all(1,2,3,4,6,7,8,9,11,12))