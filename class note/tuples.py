# t=()
# print(type(t))
# print(t)

# t=(10,20,30,40)
# print(type(t))
# print(t)

# t=(10,20,30,40,70,10)
# print(t)

# t=(10,20,30,40,70,10, "Hello", 10.5)
# print(t[1])
# print(t[:])

# t=10,20,30,
# print(type(t))


#single value tuple
# t= ()
# print(t)
# t= (10,)
# print(t)

#Multi value tuple
# t=(10,20,30)
# print(t)
# t= 10,20,30
# print(t)

# l=[10,20,30,40,66]
# t=tuple(l)
# print(type(t))
# print(t)

#indexing
# t=(10,20,30,40)
# print(t[0])
# print(t[-4])
# print(t[40])

#slicing
# t=(10,20,30,40)
# print(t[:])
# print(t[2:4])
# print(t[40])

# t=(10,20,30,40)
# t[0] = 200
# print(t)

# t1=(10,20,30,40)
# t2=(100, 200,300,400)
# print(t1 + t2)
# print(t1 + (90,))

# t1=(10,20,30,40)
# print(t1 * 2)

# t1=(10,20,30,40)
# t2=(100, 200,300,400)
# print(t2 == t1)
# print(t1!= t2)

# t1=(10,20,30,40)
# t2=(100, 200,300,400)
# print(10 in t1)
# print(10 not in t1)
# print(10 not in t2)

# t1=(10,20,30,40)
# t2=(100, 200,300,400)
# print(t1<t2)
# print(t1<=t2)
# print(t1>t2)
# print(t1>=t2)

t=(x for x in range(1,26) if x%2==0)
print(tuple(t))
print(type(t))
