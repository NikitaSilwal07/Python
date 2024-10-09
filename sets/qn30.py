#30.How do you use sets to solve a problem involving unique combinations or duplicates?
l=[10,20,30,40,50,60,30,55,67]
#To remove duplicate 
s=set(l) 
print(s) 
l=list(s) 
unique_list=[] 
#To create unique combination 
for i in range(len(l)): 
    for j in range(i,len(l)): 
      unique_list.append([l[i],l[j]]) 
print([set(subset) for subset in unique_list]) 