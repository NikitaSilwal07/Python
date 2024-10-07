#25. How would you find pairs of elements in a list that sum up to a specific number?
l=[3,6,9,12,15,18,21,24,27,30]
user_input=int(input("Enter number: ")) 
pairs=[] 
for i in range(len(l)): 
    for j in range(i+1,len(l)): 
     if l[i]+l[j]==user_input: 
      pairs.append([l[i],l[j]]) 
print(pairs) 