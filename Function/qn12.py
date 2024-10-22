#12.Write a function remove_duplicates(lst) that removes duplicate elements from a list.
def remove_duplicates(list): 
    non_duplicate_list=[] 
    for elements in list: 
       if elements not in non_duplicate_list: 
            non_duplicate_list.append(elements) 
    return non_duplicate_list 
l=[0,1,2,3,4,5,6,7,8,9,2,4,6,8,9,6,9,0,2,8,8,5,2,9]

print(f"The list without duplicate is : {remove_duplicates(l)}") 