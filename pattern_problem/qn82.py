for i in range(3):
    for j in range(i+1):
        print("*",end="")
    print(end=" ")
    for j in range(3-i):
        print("*",end="")
    print(end=" ")
    for j in range(3-i):
        print("*",end="")
    print(end=" ")
    for j in range(i+1):
        print("*",end="")
    print(end=" ")
    print()