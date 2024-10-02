# Q. WAP to print prime number.
userInput=int(input("Enter a number: "))
count=0
for i in range(1,userInput+1):
    if(userInput%i==0):
        count+=1

if (count==2):
    print("The number is prime.")
else:
    print("The number is not prime.")