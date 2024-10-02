# Q. WAP to find armstrong number.
userInput = int(input("Enter a number upto which armstrong is to be found : "))
print(f"Armstrong numbers up to {userInput}:")
for i in range(1,userInput):
    temp= i
    armstrong=0
    while (temp>0):
        digit=temp%10
        armstrong = armstrong+digit**3
        temp //= 10
    if(armstrong==i):
        print(i,end=" ")
