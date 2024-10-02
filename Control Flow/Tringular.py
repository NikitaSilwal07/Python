#Q. WAP to find Triangular number.
userInput=int(input("Enter a number upto where triangular number is to be found : "))
print("Triangular numbers are:")
n = 1
triangular_number = 0
while triangular_number <= userInput:
    triangular_number = n * (n + 1) // 2  # Calculate the nth triangular number
    if triangular_number <= userInput:
        print(triangular_number, end=" ")
    n += 1