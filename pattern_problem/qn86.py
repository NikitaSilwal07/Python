for i in range(1,6):
    for j in range(i):
        print(j+1,end="")
    if i!=1:
        for j in range(i-1,0,-1):
            print(j,end="")
    print()