#24. How would you find the second largest element in a list without using built-in sorting functions?
l=[10,64,57,47,3,90,8,11,22,15] 
sorted_list=[] 
for item in l: 
     i=0 
     for x in sorted_list: 
         if item<x: 
             sorted_list.insert(i,item) 
             i+=1 
             break 
         i+=1 
     else: 
         sorted_list.append(item)

print(f"The second largest element is :{sorted_list[-2]}") 
