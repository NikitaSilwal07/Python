n=6
p=65
for i in range(n):

    for j in range(i,n):
        print(" ", end = ' ')

    for j in range(i):
        print(chr(p+j), end = ' ')   

    for j in range(i-2,-1,-1):
        print(chr(p+j), end = ' ')    
     
    print(' ')