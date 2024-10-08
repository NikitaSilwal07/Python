#9. How do you unpack values from a tuple into variables?
t=(10,20,30,40,50)
a,b,c,d,e=t
print(a,b,c,d,e)
print(type(a))

t=(10,20,30,40,50)
a,*b=t
print(a,b)