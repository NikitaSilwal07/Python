#21. How would you rotate a list by n positions to the left?
l=[10,20,30,40,50,60] 
user_input=int(input("Enter n to rotate elements to left: ")) 
rotated_list=l[user_input:]+l[:user_input] 
print(rotated_list) 