# Q. WAP to find Twin number.
userInput=int(input("Enter a number upto where twin number is to be found : "))
print("The twin numbers are : ")
previous=-1
for i in range(1,userInput+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if count==2:
        if(i-previous==2):
            print(f"({previous},{i})")
        previous=i