# 24. Write a program to find the frequency of each character in a string.

user_input=input("Enter a string: ")
characters_count={}
for characters in user_input:
    if characters in characters_count:
        characters_count[characters]+=1
    else:
        characters_count[characters]=1

for character,count in characters_count.items():
    print(f'{character}: {count}')