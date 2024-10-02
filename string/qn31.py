#31. Write a Python program that counts how many times each vowel appears in a given string.
user_input=input("Enter a string: ")
characters_count={}
for x in user_input:
    if x=='a'or  x=='e' or  x=='i'or x=='o'or x=='u'or x=='A'or x=='E'or x=='I'or x=='O'or x=='U':
        if x in characters_count:
            characters_count[x]+=1
        else:
            characters_count[x]=1
for character,count in characters_count.items():
    print(f'{character}: {count}')