for i in range(1,5):
    if i==1:
        print(1,end="")
    else:
        for j in range(i):
            if j+1!=i:
                print(i,end="*")
            else:
                print(i,end="")
    print()
for i in range(4,0,-1):
    if i==1:
        print(1,end="")
    else:
        for j in range(i):
            if j+1!=i:
                print(i,end="*")
            else:
                print(i,end="")
    print()