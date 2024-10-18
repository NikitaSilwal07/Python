#15. How do you sort a dictionary by its values?
d={500:"Nikita",200:"Nikesh",100:"Isha",400:"Archana"}
sorted_d=dict(sorted(d.items(),key=lambda item:item[1])) 
print(sorted_d) 