#13. String, Tuple, & List: Given a string, convert it into a list of tuples where each tuple contains
#  a character and its index in the string.

string="My name is Nikita" 
l=[] 
index=0 
for char in string: 
    l.append((char,index)) 
    index+=1 
print(l) 