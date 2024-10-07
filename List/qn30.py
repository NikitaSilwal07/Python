#30. How would you find the majority element in a list (the element that appears more than half the time)?

l1=[2,2,5,2,2,2,3,4,9,2,3,1,2,2,4,2,2,7,8,2,3,2,5,6,2,2,9] 
majority_number=len(l1)//2 
for items in l1: 
    if l1.count(items)>majority_number: 
     print(f"The number that appear majority of time is: {items}") 
     break 
else: 
     print("No number occur in majority") 