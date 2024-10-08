#16.How do you sort a list of tuples based on the second element in each tuple?

list_of_tuple=[(8,4,5),(1,2),(4,7,8),(5,3),(6,8),(9,0)] 
for i in range(len(list_of_tuple)):  
    for j in range(0, len(list_of_tuple)-i-1): 
      if list_of_tuple[j][1] > list_of_tuple[j + 1][1]: 
        list_of_tuple[j], list_of_tuple[j + 1] = list_of_tuple[j + 1], list_of_tuple[j] 
print(list_of_tuple) 