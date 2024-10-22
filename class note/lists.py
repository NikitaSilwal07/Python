# a=[] 
# print(type(a)) 
# a=[10,20,"30",50.5,"43",20,30] 
# print(a) 
# print(type(a)) 
# a.append("hello") 
# a.remove(30) 
# print(a) 

# a=[] 
# print(type(a)) 
# a=[10,20,"30",50.5,"43",20,30] 
# print(a) 
# print(type(a)) 
# user=eval(input("Enter list: ")) 
# print(user) 
# print(type(user)) 
# l=list(range(10,20)) 
# print(l) 
# print(type(l)) 
# string=list("Python") 
# print(string) 
# print(type(string)) 
# string="Learning Python is beautiful." 
# lists=string.split(" ") 
# print(lists) 
# print(type(lists)) 

# lists=[10,20,30,40,50,60] 
# print(lists[2]) 
# print(lists[-4]) 
# # print(lists[-8]) Out of range 

# lists=[10,20,30,40,50,60] 
# print(lists[1:5]) 
# print(lists[1:5:2]) 
# print(lists[6:2:-2]) 
# print(lists[4:1000:1]) 

# lists=[10,20,30,40,50,60] 
# print(lists) 
# print(id(lists)) 
# lists[1]=70 
# print(lists) 
# print(id(lists)) 

# Traversing of list 
# 1. By using while  
# lists=[10,20,30,40,50,60] 
# i=0 
# while i<len(lists): 
#     print(lists[i]) 
#     i+=1 
# print() 
# 2. By using for loop 
# a=[10,20,"30",50.5,"43",20,30] 
# for item in a: 
#     print(item,end='\t') 

# lists=[10,20,30,40,50,60,10,50,40,50,60,30,50,10,50,20,10,10,1,10] 
# length=len(lists) 
# print(f"Length is {length}.") 
# count_number=lists.count(10) 
# print(f"Count of 10 is : {count_number}") 
# index_number=lists.index(40) 
# print(f"Count of 40 is : {index_number}") 

# a=[10,20,"30",50.5,"43",20,30] 
# a.append(80) 
# a.append('Join') 
# print(a) 
 
# lists=[] 
# for i in range(0,101): 
#     if i%10==0: 
#         lists.append(i) 
# print(lists) 


# a=[10,20,"30",50.5,"43",20,30] 
# a.insert(1,123) 
# a.insert(5,"Hello") 
# print(a) 

# a=[10,20,"30",50.5,"43",20,30] 
# lists=[10,20,30,40,50,60] 
# a.extend(lists) 
# print(a,len(a)) 
# a=[10,20,"30",50.5,"43",20,30] 
# lists=[10,20,30,40,50,60] 
# a.append(lists) 
# print(a,len(a)) 
# a=[10,20,"30",50.5,"43",20,30] 
# b="Hello" 
# a.extend(b) 
# print(a) 

# a=[10,20,"30",50.5,"43",20,30] 
# a.remove("30") 
# print(a) 
# a.remove(30) 
# print(a) 
# a.remove("Hello") Output: Value Error 

# lists=[10,20,30,40,50,60,10,50,40,50,60,30,50,10,50,20,10,10,1,10] 
# x=int(input("Enter number to remove: ")) 
# while True: 
#     if x in lists: 
#         lists.remove(x) 
#     else: 
#         break 
# print(lists) 

# a=[10,20,"30",50.5,"43",20,30] 
# a.pop() 
# print(a) 
# a.pop(3) 
# print(a) 

# a=[10,20,"30",50.5,"43",20,30] 
# a.reverse() 
# print(a) 
 
# a=[10,20,"30",50.5,"43",20,30] 
# b=reversed(a) 
# for i in b: 
#     print(i,end=" ") 

# lists=[10,20,3,40,50,640,10,502,40,5,60,30,50,10,50,20,10,10,1,10] 
# lists.sort() 
# print(lists) 
 
# l=["Hello","Python","is","fun."] 
# l.sort() 
# print(l) 
 
# lists=[10,20,3,40,50,640,10,502,40,5,60,30,50,10,50,20,10,10
#  ,1,10] 
# lists.sort(reverse=True) 
# print(lists) 

# Aliasing 
# x=[10,20,30,40] 
# y=x 
# print(id(x)) 
# print(id(y)) 
# y[0]=20 
# print(x) 
# print(y) 
# print(id(x)) 
# print(id(y)) 

# a. slice operator 
# x=[10,20,30,40] 
# y=x[::] 
# print(id(x)) 
# print(id(y)) 
# y[0]=20 
# print(x) 
# print(y) 
# print(id(x)) 
# print(id(y)) 

# b. copy function 
# x=[10,20,30,40] 
# y=x.copy() 
# print(id(x)) 
# print(id(y)) 
# y[0]=20 
# print(x) 
# print(y) 
# print(id(x)) 
# print(id(y)) 

# x=[10,20,30,40] 
# x.clear() 
# print(x) 

# x=[10,20,30,40] 
# y=[100,200,300,400] 
# print(x+y) 
# # print(x+300) Not possible 
# print(x+[300]) 

# x=[10,20,30,40] 
# print(x*2) 

# x=[10,20,30,40] 
# y=[10,20,30,40] 
# print(x==y) 
# y=[40,20,30,40] 
# print(x==y) 
# x=["Dog","Cat","Rat"] 
# y=["Dog","Cat","Rat"] 
# z=["DOG","CAT","RAT","Bat"] 
# print(x==y) 
# print(x==z) 
# print(x!=z) 

# y=[100,200,300,400] 
# print(100 in y) 
# print(10 not in y) 

# y=[100,200,300,400,[10,20,30,40]] 
# print(y[0]) 
# print(y[4]) 
# print(y[4][2]) 

# x=[[1,2,3],[4,5,6],[7,8,9]] 
# print(x) 
# print("Row Wise:") 
# for elements in x: 
#     print(elements) 
 
# print("Matrix Wise:") 
# for elements in x: 
#     for items in elements: 
#         print(items,end=" ") 
#     print() 

# l=[x for x in range(1,11)] 
# print(l) 

# words=["Nikita","sita","Shyam","isha","Nanita","Zen"] 
# l=[w[0] for w in words] 
# print(l) 
 
# y=[101,20,235,300,34,234,52,532,3,354,23,52,400] 
# m=[items for items in y if items%2==0] 
# print(m) 

# strings="The quick brown fox jumps over the lazy dog".upper() 
# lists=strings.split() 
# final_list=[[x,len(x)] for x in lists] 
# print(final_list) 

# t1= (100,200,300,400)
# print(len(t1))
# print(t1.count(100))
# print(t1.index(200))

# t2=(100, 200,300,40,200,200)
# t3=sorted(t2)
# print(t3)
# r=reversed(t2)
# t2 = tuple(r)
# print(t2)

# print(min(t1))
# print(max(t2))

#packing 
# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t)
# print(type(t))

#unpacking
# t= (10,20,30,40)
# a,b,c,d=t
# print(a,b,c,d)


