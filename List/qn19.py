#19. How would you flatten a list of lists into a single list (without using any built-in functions)?
l=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]] 
single_list=[] 
for lists in l: 
  for items in lists: 
    single_list.append(items) 
print(single_list) 