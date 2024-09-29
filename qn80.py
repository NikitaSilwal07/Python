for i in range(1,6):
    for j in range(i):
        if (i%2==0 and (j+1)%2==0)or (i%2!=0 and (j+1)%2!=0):
            print(j+1,end="")
        else:
            print("*",end="")
    print()