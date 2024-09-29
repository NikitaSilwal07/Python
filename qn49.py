
n = 9
for i in range(n, 5, -1): 
    for j in range(i, n + 1):  
        print(j, end='')
    for j in range(n - 1, i - 1, -1):  
        print(j, end='')
    print()  
