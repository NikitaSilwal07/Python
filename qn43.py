k= 9
n=9
for i in range (5): 
 for j in range(i+1):
    print(k, end =' ')
    if(k>=n):
        k%=n
    else:
        k=k+1
 print(' ')