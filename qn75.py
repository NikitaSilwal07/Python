space=6
list=['','a','b','c','d','e']
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(space):
        print(end=" ")
    for j in range(i,0,-1):
        print(list[j],end="")
    space-=1
    print()