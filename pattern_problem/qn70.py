for i in range(4,0,-1):
    number=1 if i%2==0 else 3
    for j in range(i):
        print(number,end="")
        number=number+1
        if number>4:
            number=number%4
    print()

#2nd method

# number = 1
# # First row with 4 elements
# for i in range(4):
#     print(number, end="")
#     number += 1
# print() 

# # Second row with 3 elements
# number = 3  
# for i in range(3):
#     print(number, end="")
#     number += 1
#     if number > 4:  
#         number = 1
# print()  

# # Third row with 2 elements
# number = 1  
# for i in range(2):
#     print(number, end="")
#     number += 1
# print()  
# #fourth row with 1 element
# number = 3 
# print(number)  
 
