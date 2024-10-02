# Q. WAP to find Harshad number number.
userInput = int(input("Enter a number upto which Harshad series is to be found : "))
print("The harshad number are:")
for i in range(1, userInput):
    temp=i
    sum=0
    while(temp>0):
        digit=temp%10
        sum=sum+digit
        temp//= 10
    if (i%sum==0):
        print(i, end=" ")