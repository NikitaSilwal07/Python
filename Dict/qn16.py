#16. How do you get the value for a key without raising an error if the key doesn't exist?
d={100:"Nikita",200:"Nikesh",300:"Isha",400:"Archana"}
print(d.get("E","Not found")) 
print(d.get(100,"Not found")) 