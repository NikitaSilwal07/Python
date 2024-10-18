#30. How do you handle mutable objects as dictionary keys, and what problems can it cause?

# l1=[2,4] 
# l2=[1,3] 
# l3=[6,8] 
# l4=[5,7] 
# d={l1:"First two even",l2:"First two odd",l3:"Second two even",l4:"Second two odd"} 
# print(d) 


#converting it into tuples
l1=[2,4] 
l2=[1,3] 
l3=[6,8] 
l4=[5,7] 
# d={l1:"First two even",l2:"First two odd",l3:"Second two even",l4:"Second two odd"} 
# print(d) 
 
d={tuple(l1):"First two even",tuple(l2):"First two odd",tuple(l3):"Second two even",tuple(l4):"Second two odd"} 
print(d) 