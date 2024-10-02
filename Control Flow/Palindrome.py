# Q. WAP to find palindrome number.
userInput = int(input("Enter a number upto which palindrome is to be found : "))
print(f"Palindrome numbers up to {userInput}:")
for i in range(1,userInput):
    temp= i
    palindrome=0
    while (temp>0):
        digit=temp%10
        palindrome = palindrome*10+digit
        temp //= 10
    if(palindrome==i):
        print(i,end=" ")