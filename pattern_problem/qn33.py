# n = 6

# for i in range(n):
#     for j in range(n -i-1):
#         print(" ", end=' ')
#     for j in range(1, i + 2):
#         print(j, end=' ')
    
#     print(' ')

n=6
k=n-1
for i in range(1,n+1):

    for j in range(k):
        print( end = ' ')

    for j in range(1,i+1):
        print(j, end = ' ')   
  
    print(' ')
    k=k-1
