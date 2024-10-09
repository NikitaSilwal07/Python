#19.How do you freeze a set to make it immutable?
s1={10,20,30,40,"Nikita",55.5}
fs=frozenset(s1) 
print(fs) 
print(type(fs)) 