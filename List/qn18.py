#How would you create a new list that contains only the unique elements from an existing list?
l=["Hello","Python",10,20,30,40,10,40,"Hello","Py","World."] 

unique_list=[item for item in l if l.count(item)==1] 
print(unique_list)