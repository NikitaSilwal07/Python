number=1
for i in range(5):
    for j in range(i+1):
        print(number,end="")
        number+=1
        if number>1:
            number%=2
    print()