# #Q. WAP to print prime number upto n.
userInput=int(input("Enter a number upto where prime number is to be found : "))
print("The prime numbers are : ")
for i in range(1,userInput+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if count==2:
        print(i,end=" ")