#28. How do you invert a dictionary, i.e., swap keys and values?
d={100:"Nikita",200:"Nikesh",300:"Isha",400:"Archana"}
reverse_d={v:k for k,v in d.items()} 
print(reverse_d) 