n=5
p=65
for i in range(n):

    for j in range(i):
        print(" ", end = ' ')

    for j in range(i,n):
        print(chr(p+j), end = ' ')   

    for j in range(n-2,i-1,-1):
        print(chr(p+j), end = ' ')    
     
    print(' ')