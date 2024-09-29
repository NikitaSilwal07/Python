userInput=int(input("Enter number of rows : "))
first_half=userInput//2
second_half=userInput-first_half
for i in range(1,first_half+1):
    for j in range(i):
        print("*",end="")
    print()
for i in range(second_half,0,-1):
    for j in range(i):
        print("*",end="")
    print()