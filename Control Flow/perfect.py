# Q. WAP to find perfect number.
userInput = int(input("Enter a number upto which perfect number is to be found : "))
print(f"Perfect numbers up to {userInput}:")
for i in range(1,userInput):
    sum=0
    for j in range(1,i):
        if (i%j==0):
            sum=sum+j
    if sum==i:
        print(i)