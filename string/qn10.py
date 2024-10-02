# 10. Write a Python program that finds all occurrences of the letter 'a' in
#  the string "banana" and prints their positions.

string="banana"
count=0
i=1
print(f"The position of a in string : {string} are:")
for x in string:
    if x=="a":
        print(f"{i}th 'a' is in {count} index")
        i+=1
    count+=1
print(f"Total number of a is: {i-1}")