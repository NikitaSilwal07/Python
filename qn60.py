n = 4  
num = 1  
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')  
    for j in range(i + 1):
        print(num, end=' ')
        num += 1  
    print()  