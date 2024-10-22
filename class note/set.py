#s={} This is not the way to create a empty set. 
# s={} 
# s1=set(s) #Empty Set 
# print(s1) 
# print(type(s1)) 
 
# s={10,20,30,40,50,"Hello","Python"} 
# print(s) 
# print(type(s)) 
 
# s={10} #Single value set 
# print(s) 
# print(type(s)) 
 
# l=[10,560,43,43] 
# s=set(l) 
# print(s) 
 
# s=range(10) 
# sq=set(s) 
# print(sq) 
# print(type(sq)) 


# s={20,40,"Hello","Python",20} 
# print(s) 

# s={10,20,30,40}
# s.add(50)
# print(s)
# s.update(range(50))
# print(s)

#Aliasing and cloning
# s={10,20,30,40,"Hello","Nikita"} 
# s1=s.copy()
# print(s1) 
# print(s) 
# s.add(67) 
# print(s1) 
# print(s) 

# s={10,20,30,40,50,"Nikita"}
# s.pop()
# print(s)

# s={10,20,30,40,50,"Nikita"}
# s.remove(20)
# print(s)


# s={10,20,30,40,50,"Nikita"}
# s.discard(20)
# print(s)

# s={10,20,30,40,50,"Nikita"}
# s.clear()
# print(s)

# x={20,40,"Hello","Python"} 
# y={"Hello",40,89,90,"Programming"} 
# #UNION 
# print(x.union(y)) 
# #INTERSECTION 
# print(x.intersection(y)) 
# #DIFFERENCE 
# print(x.difference(y)) 
# #SYMMETRIC DIFFERENCE 
# print(x.symmetric_difference(y)) 

# x={10,20,30,40,50,"Hello","nikita"} 
# y={"Hello",40,89,90,"Programming"} 
# print(20 in x) 
# print(20 in y) 
# print("Programming" in x) 
# print("Programming" in y) 

# s={x for x in range(40) if x%2==0} 
# print(s) 
