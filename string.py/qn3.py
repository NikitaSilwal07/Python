# #3. Write a Python program that counts the number of vowels in a given string.


user_input=input("Enter a string: ")
count=0
for  x in user_input:
    if x=='a'or  x=='e' or  x=='i'or x=='o'or x=='u'or x=='A'or x=='E'or x=='I'or x=='O'or x=='U':
        count=count+1
print(f"Number of vowel in string is: {count}")