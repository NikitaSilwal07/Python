#20. How do you get a dictionary’s items as a list of tuples?

d={100:"Nikita",200:"Nikesh",300:"Isha",400:"Archana"}
dic_items=[(k,v) for k,v in d.items()] 
print(dic_items) 