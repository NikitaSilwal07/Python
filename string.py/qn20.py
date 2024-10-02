# 20. Find the longest word in a given string.

user_input=input("Enter a string: ")
words=user_input.split()
longest_string=""
previous_count=0
for word in words:
    if len(word)>len(longest_string):
        longest_string=word
        previous_count=len(word)

print(f'Longest string is {longest_string} with {previous_count} characters.')