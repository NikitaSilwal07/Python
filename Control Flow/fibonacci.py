#  Q WAP to find fibonacci series.
userInput = int(input("Enter a number upto which fibonacci series is to be found : "))
print(f"fibonacci series up to {userInput}:")
first_number=0
second_number=1
print(first_number,second_number, end=" ")
i=2
while(i<=userInput):
    next_number=first_number+second_number
    print(next_number,end=" ")
    first_number=second_number
    second_number=next_number
    i+=1