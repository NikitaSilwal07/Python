for i in range(1,5):
    number=i
    for j in range(4):
        print(number,end="")
        number+=1
        if(number>4):
            number%=4
    print()