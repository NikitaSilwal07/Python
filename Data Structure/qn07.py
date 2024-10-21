#7. Dictionary & Tuple: Given a dictionary, return a
#  sorted list of tuples where each tuple is a key-value pair from the dictionary, 
# sorted by the dictionary’s values.

d={100:"Nikita",700:"sumita",300:"Isha", 200:"Vaskar",500:"Ayush"} 
l=[] 
for k,v in d.items(): 
    l.append((k,v)) 
sorted_list=sorted(l,key=lambda item:item[1]) 
print(sorted_list) 