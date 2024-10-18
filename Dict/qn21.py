#21. How do you create a dictionary with default values for missing keys?

d={100:"Nikita",200:"Nikesh",300:"Isha",400:"Archana"}
(d.setdefault(100,"Angry")) 
print(d) 
d={100:"Nikita",200:"Nikesh",300:"Isha",400:"Archana",500:"Rabina"}
(d.setdefault(600,"Angry")) 
print(d) 