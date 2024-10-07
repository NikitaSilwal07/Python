#26. How would you remove duplicates from a list while preserving the original order?
l=["Hello","Nikita",10,20,30,40,10,40,"Hello","Python","6","20"] 
no_duplicate=[] 
for items in l: 
    if items not in no_duplicate: 
     no_duplicate.append(items) 
print(no_duplicate) 