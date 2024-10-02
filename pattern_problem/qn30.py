n=5
k=6
for i in range(n):

    for j in range(k):
        print( end = ' ')

    for j in range(i+1,0,-1):
        print(j, end = ' ')   
  
    print(' ')
    k=k-1