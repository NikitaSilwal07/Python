# import modules 
 
# modules.add(4,5) 

# import modules as m 
# m.add(50,60) 
# m.product(10,20) 
# modules.add(10,20) This throws an error after aliasing.

# from modules import add,product 
# add(10,20) 
# product(2,49)

# from modules import add,product as p
# add(10,50)
# p(20,40) 

# from function import *
# from modules import fact 
# fact(5) 

# from function import fact as fun 
# from modules import fact as mod 
# fun(4) 
# mod(4) 

# import modules 
# import time 
 
# modules.fact(5) 
# print("Sleep on:") 
# time.sleep(15) 
# print("Sleep off") 
# import modules 
# modules.fact(5) 

# def fact(n): 
#     # print("Before sleep") 
#     print("After sleep") 

# def fact(n): 
#     # print("Before sleep") 
#     print("After sleep") 

# import modules 
# import time 
# from importlib import reload 
# modules.fact(5) 
# print("Sleep on:") 
# time.sleep(15) 
# print("Sleep off") 
# reload(modules) 
# modules.fact(5) 

# import time 
# print(dir(time)) 

# import time 
# help(time) 

# import math 
# print(dir(math)) 

# import math 
 
# print(math.floor(4.2)) 
# print(math.sin(49)) 
# print(math.sinh(49)) 

# import random 
 
# print(random.random()) 
# print(random.randint(1,6)) 

# import random 
# print(random.uniform(100,200)) 

# import random 
# print(random.randrange(10)) 
# print(random.randrange(4,10)) 
# print(random.randrange(1,10,2)) 

# import random 
# l=["nikita","nita","sonu","sabita","Sarita"] 
# print(random.choice(l)) 

#OTP generation(6 number) 
import random 
otp='' 
for i in range(6): 
    otp=otp+str(random.randint(0,9)) 
print(otp) 