k=4
for i in range(4):
    for j in range(k):
        print(end="")
    for j in range(i*2+1):
        print("*",end="")
    print()
    k=k-1
k=k+1
for i in range(3,0,-1):
    k=k+1
    for j in range(k):
        print(end="")
    for j in range(i*2-1):
        print("*",end="")
    print()