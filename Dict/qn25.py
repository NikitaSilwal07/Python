#25.How do you combine two dictionaries, summing values for common keys?

d1={100:"Nikita",200:"Nikesh",300:"Isha",400:"Archana"}
d2={500: 'Prabin', 900: 'Hira', 300: 'Pant', 200: 'Siwal'} 
common_dict={} 
for k,v in d1.items(): 
   common_dict[k]=v 
for k,v in d2.items(): 
    if k in common_dict: 
       common_dict[k]+=v 
    else: 
       common_dict[k]=v 
print(common_dict) 