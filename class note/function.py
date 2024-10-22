# def calculate(a,b):
#     print("The sum of a and b is", a+b)
#     print("The difference of a and b is", a-b)
#     print("The product of a and b is", a*b)
#     print("The division of a and b is", a/b)

# calculate(20,10)
# calculate(200,100)
# calculate(2000,1000)

# def hello(): 
#      print("Hello") 
# hello() 
# hello() 

# def hello(name): 
#     print("Hello",name) 
# hello("Nikita") 
# hello("Nikesh") 

# def square(num): 
#     print("The Square number of he given number is :",num*num) 
# square(4) 
# square(5) 

# def add(a,b): 
#     sum=a+b 
#     return sum 
# a=add(20,10) 
# print(a) 
# or
# print("The sum is:", add(20,10))

# def square(num): 
#     print("Square number of the given number is:",num*num) 
# a=square(6) 
# print(a) 

# def oddeven(num): 
#     if num%2==0: 
#         print(num,"is even.") 
#     else: 
#         print(num,"is odd.") 
 
# oddeven(4) 
# oddeven(3)  

# def fact(num): 
#     result=1 
#     while num>=1: 
#       result=result*num 
#       num=num-1 
#     return(result) 
 
# a=fact(3)
# print(a)
# print(fact(4))

# def calculate(a,b): 
#     sum=a+b 
#     sub=a-b 
#     return sum,sub 
# a,b=calculate(8,5) 
# print("The sum is :",a) 
# print("The sub is :",b) 

# def sub(a,b): 
#    print(a-b) 
# sub(20,10)#Here a=20,b=10 id defined by positional argument 
# sub(10,20)#Here a=10,b=20 id defined by positional argument 
# sub(10,30) #Positional argument throws error 

# def sub(a,b): 
#     print(a-b) 
 
# sub(a=20,b=10) 
# sub(b=10,a=20) 
# sub(20,b=10) #Valid 
# sub(a=20,10)# Invalid 

# def hello(name="Guest"): 
#     print(f"Hello {name}") 
 
# hello("Nikita") 
# hello() 

# def hello(name="Guest",msg="Goodnight"):
#      print(f"hello {name}, {msg}") 
 
# hello("Nikita") 
# hello() 
# # hello(,"Good night")#Not valid 
# hello(msg="Good night")

# def hello(*a): 
#     print(a) 
# hello(10) 
# hello(20,30) 
# hello(30,40,50)  

# def f(*a): 
#     print(a) 
#     print(type(a)) 
 
# f((10,20),(30,40)) 

# def addition(*a): 
#     sum=0 
#     for x in a: 
#         sum=sum+x 
#     print (f"The sum is: {sum}") 
 
# addition() 
# addition(10,20) 
# addition(1,2,3,4,5) 

# def f(a,*args): 
#     print(a) 
#     print(args) 
 
# f(19) 
# f(10,12,13,14,15,16,17,18,19) 

# def f(**kwargs): 
#     for k,v in kwargs.items(): 
#         print(k,'----',v) 
 
# f(a=10,b=20,c=30,d=67) 
# f(v=19) 

# def f(*args,**kwargs): 
#     print(args) 
#     print(kwargs) 
 
# f(20,30,40,50,60,a=10,b=20,c=30,d=67) 

# k=10 
# def f1(): 
#     print(k) 
# def f2(): 
#     print(k) 
# f1() 
# print(k) 
# f2() 


# def f1(): 
#     a=10 
#     print(a) 
 
# f1() 
# # print(a) Not possible 

# def f1(): 
#     # global a=10 Not valid this way 
#     global a 
#     a=10 
#     print(a) 
 
# def f2(): 
#     print(a) 
# f1() 
# f2() 
# print(a) 

# a=20 
# def f(): 
#     a=10 
#     print(a) 
 
# f() 
# print(a) 

# Gives error 
# def f1(): 
#     a=10 
#     global a 
#     print(a) 

# a=10 #  Global variable 
# def f(): 
#   a=87 #Local variable 
# print(globals()['a']) 
# f() 

# def fact(n): 
#   if n==0: 
#     return 1 
#   else: 
#     return n*fact(n-1) 
# print("The factorial of 5 is: ",fact(5)) 


# s=lambda n:n*n 
# print("The square is : ",s(4)) 
# print("The square is : ",s(5)) 
# sum=lambda a,b:a+b 
# print("The sum is : ",sum(5,4)) 


# biggest=lambda a,b:a if a>b else b 
# print(biggest(10,20)) 
# largest=lambda a,b,c:a if a>b and a>c else b if b>c else c 
# print(largest(10,5,11)) 

# The following code is making filter function from scratch 
# l=[x for x in range(15)] 
# def isEven(n): 
#     if n%2==0: 
#         return True 
#     else: 
#         return False 
# l1=[] 
# for n in l: 
#     if isEven(n)==True: 
#         l1.append(n) 
# print(l1) 

# Using Filter function 
# l=[x for x in range(15)] 
# def isEven(n): 
#     if n%2==0: 
#         return True 
#     else: 
#         return False 
 
# l1=list(filter(isEven,l)) 
# print(l1) 

# Filter with lambda function 
# l=[x for x in range(15)] 
# l1=list(filter(lambda x:x%2==0,l)) 
# print(l1) 

# l=[1,2,3,4,5] 
# def square(n): 
#     return n*n 
 
# l1=list(map(square,l)) 
# print(l1) 

# Map function with lambda function 
# l=[1,2,3,4,5] 
# l1=list(map(lambda x:x*x,l)) 
# print(l1) 

# Map with two sequences 
# l=[1,2,3,4,5] 
# m=[6,7,8,9,10] 
# l1=list(map(lambda x,y:x+y,l,m)) 
# print(l1) 

# from functools import reduce 
# l=[1,2,3,4,5,6] 
# result=reduce(lambda x,y:x+y,l) 
# print(result) 

# def hello(name): 
#     print("Hello",name) 
 
# wish=hello 
# hello("Nikita") 
# wish("Nikesh") 
# del hello 
# hello("Hira") After deleting not possible to call from 
# hello but possible from wish 
# wish("Laxmi")

# def outer(): 
#     print("Outer function") 
#     def inner(): 
#         print("Inner function") 
#     print("Below inner function and out of inner function.") 
#     inner() 
 
# outer() 
# # inner() Cannot be accessed from here

# def outer(): 
#     print("Outer function") 
#     def inner(): 
#         print("Inner function") 
#     print("Below inner function and out of inner function.") 
#     return inner 
 
# f1=outer() 
# f1() 

