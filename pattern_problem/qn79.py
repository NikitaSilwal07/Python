for i in range(1,5):
    if i==1 or i==4:
        print("*"*6,end="")
    else:
        print('*',end="")
        for j in range(4):
            print(end=" ")
        print('*',end="")
    print()