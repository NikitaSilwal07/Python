# Q. WAP to find fibonacci series.
userInput = int(input("Enter a number which is to know whether it lies in fibonacci series or not : "))
first_number=0
second_number=1
if(userInput==first_number or userInput==second_number):
    print(f"{userInput} is a part of Fibonacci series.")
else:
    while(second_number<userInput):
        next_number=first_number+second_number
        first_number=second_number
        second_number=next_number
    if(next_number==userInput):
        print(f"{userInput} is a part of Fibonacci series.")
    else:
        print(f"{userInput} is not a part of Fibonacci series.")