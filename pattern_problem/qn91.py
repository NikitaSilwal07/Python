space=0
for i in range(5,0,-1):
    number=i
    for j in range(space):
        print(end=" ")
    for j in range(i):
        print(number,end="")
        number-=1
    number+=1
    for j in range(i-1):
        number+=1
        print(number,end="")
    print()
    space+=1