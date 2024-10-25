a=555 
 
def add(a,b): 
    print("The sum is : ",a+b) 
 
def product(a,b): 
    print("The product is : ",a*b) 


def fact(num): 
    result=1 
    while num>=1: 
      result=result*num 
      num=num-1 
    return(result) 
 
a=fact(3)
print(a)
print(fact(4))    