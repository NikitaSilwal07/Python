for i in range(3,0,-1):
    for j in range(3,0,-1):
        if i==j:
            break
        else:
            print(j,end="")
    for j in range(i*2-1):
        print(i,end="")
    for j in range(i,4):
        if i==j:
            continue
        else:
            print(j,end="")
    print()    
for i in range(2,4):
    for j in range(i+1,4):
        if j==i:
            continue
        else:
            print(j,end="")
    for j in range(i*2-1):
        print(i,end="")
    for j in range(2,4):
        if i==j:
            print(i+1,end="")
        else:
            break
    print()