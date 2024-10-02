for i in range(1,5):
    output=i
    for j in range(i):
        print(output,end="")
        output=output+1
    output=output-1
    for j in range(i,1,-1):
        output-=1
        print(output,end="")
    print()
