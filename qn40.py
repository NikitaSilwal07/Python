n = 5  
for i in range(n):
    print(" " * (n - i - 1), end='')
    for j in range(i + 1):
        print(chr(65 + j), end=' ')
    print() 

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end='')
    for j in range(i):
        print(chr(65 + j), end=' ')
    
    print() 
