# Q. WAP to print strong number.
import math
userInput = int(input("Enter a number up to where strong numbers are to be found: "))
print(f"Strong numbers up to {userInput}:")
for i in range(1, userInput + 1):
    sum_of_factorials = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        factorials=1
        for j in range(1, digit+1):
            factorials *=j
        sum_of_factorials +=factorials
        temp //= 10
    if sum_of_factorials == i:
        print(i)