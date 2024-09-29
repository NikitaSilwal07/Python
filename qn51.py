n = 5
for i in range(1, n + 1):

    for j in range(n - i + 1, n + 1):
        print(j, end='')
 
    for j in range(n - 1, n - i, -1):
        print(j, end='')
    print()
