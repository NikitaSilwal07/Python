#18. How do you find the key with the maximum value in a dictionary?

d={100:"Nikita",200:"Nikesh",300:"Isha",400:"Archana"}
max_value=max(d.values()) 
k=[k for k,v in d.items() if v==max_value][0] 
print(f"Maximum value is {max_value} and its key is: {k}") 