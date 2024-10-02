n=4
p= 65
for i in range(0,n):
    for j in range(i+1):
        print(chr(p), end = " ")
    p+=1
    print(' ')
p=p-1
for i in range(n-1,0,-1):
    p-=1
    for j in range(i):
        print(chr(p), end = " ")
    
    print(' ')