list=['A','B']
start=0
for i in range(0,5):
    for j in range(i+1):
        print(list[start],end="")
        if start>=1:
            start=(start+1)%2
        else:
            start=start+1
    if i%2==0:
        start=1
    else:
        start=0
    print()