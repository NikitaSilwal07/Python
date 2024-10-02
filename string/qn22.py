# 22.	Write a program that removes punctuation from a string.

punctuation=['.',',',"'",'"', '?','!','-','(',')','{','}','[',']','...',':',';']
user_input=input("Enter a string: ")
changed=""
for char in user_input:
    if char == char in punctuation:
        changed+=""
    else:
        changed+=char

print(f"Changed Character: {changed}")