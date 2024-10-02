k=3
for i in range(1,5):
    for j in range(k):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(1,i):
        if i==j:
            break
        else:
            print(j+1,end="")
    print()
    k=k-1
k=k+1
for i in range (3,0,-1):
    k=k+1
    for j in range(k):
        print(end=" ") 
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()