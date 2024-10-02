# 32. Write a program to find the shortest word in a string.

user_input=input("Enter a string: ")
words=user_input.split()
shortest_word=words[0]
for word in words:
    if len(word)<len(shortest_word):
        shortest_word=word

print(f"Shortest word is: {shortest_word}")