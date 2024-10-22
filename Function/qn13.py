#13.Write a function merge_two_lists(lst1, lst2) that merges two lists into one.

def merge_list(lst1,lst2): 
    merged_list=lst1.copy() 
    for x in lst2: 
        merged_list.append(x) 
    return merged_list 
l1=[1,4,5,6,7] 
l2=[11,14,15,18] 
print(f"The merged list is: {merge_list(l1,l2)}") 