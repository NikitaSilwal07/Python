#1. String & List: Given a sentence, split the sentence into words, 
# remove duplicate words (maintaining the order), and return the result as a list.

s="Python is fun to learn and Nikita is enjoying to learn it .".split()
final_list=[] 
for word in s: 
    if word in final_list: 
     continue 
    else: 
     final_list.append(word) 

print(final_list) 