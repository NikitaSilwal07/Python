#22.How do you perform element-wise addition of two tuples of the same length?

t1=(4,5,7,8,9) 
t2=(10,1,2,3,6,) 
sum=[] 
if (len(t1))==len(t2): 
    for i in range(len(t1)): 
     sum.append(t1[i]+t2[i]) 
    else: 
      print("Two tuples are not of same length.") 
sum=tuple(sum) 
print(sum) 
print(type(sum)) 