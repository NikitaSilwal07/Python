n = 6
for i in range(n):

    for j in range(n - i):
        print(chr(65 + j), end='')  

    for j in range(n - i - 1, -1, -1):
        print(chr(65 + j), end='')

    print()
