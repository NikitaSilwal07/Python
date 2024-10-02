for i in range(3, 0, -1):
    for j in range(4): 
        if i == 3:
            print(1 if j == 0 else 3, end="")  
        elif i == 2:
            print(i, end="")  
        elif i == 1:
            print(3 if j < 3 else 1, end="")  
    print()  
