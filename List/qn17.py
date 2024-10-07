#17. Given two lists, how would you find the common elements between them?
l1=[10,20,30,40,50,60] 
l2=[20,40,6,8,10] 
common_list=[] 
for item in l1: 
   if item in l2: 
      common_list.append(item) 
print(common_list) 