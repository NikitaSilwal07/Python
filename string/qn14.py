
# 14. Check if two strings are anagrams of each other (contain the same letters in different orders).

user_input1=input("Enter a string1: ")
user_input2=input("Enter a string2: ")
if sorted(user_input1)==sorted(user_input2):
    print(f"{user_input1} and {user_input2} are anagram.")
else:
    print(f"{user_input1} and {user_input2} are not anagram.")