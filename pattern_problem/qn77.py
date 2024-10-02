number=['0','1']
for i in range(1,6):
    start=i%2
    for j in range(i):
        print(number[start],end="")
        start=start+1
        if start>=2:
           start=start%2
    print()