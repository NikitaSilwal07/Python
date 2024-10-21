#2. List & Dictionary: Given a list of numbers, create a dictionary where each key is a number
#  and the value is its frequency in the list.
l=[1,2,3,4,5,6,7,2.3,8,9,0,44,0,54,1,4,6,66]
d={}

for num in l: 
    if num in d: 
     d[num]+=1 
    else: 
      d[num]=1 
print(d) 