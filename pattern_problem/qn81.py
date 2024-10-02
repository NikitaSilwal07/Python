lists=['','A','B','C','D','E','F']
number=1
string=1
for i in range(1,6):
    if i%2==0:
        for j in range(i):
            print(lists[string],end="")
            string+=1
    else:
        for j in range(i):
            print(number,end="")
            number+=1
    print()
