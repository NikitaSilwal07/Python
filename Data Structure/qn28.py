#28. List, Dictionary, & Set: Given a list of tuples (name, score), create a dictionary where the keys 
# are the names, andthe values are the scores, then return a set of names whose 
# scores are above a certain threshold.

l=[("Jenny", 85), ("Prabu", 90), ("Nikita", 78), ("Shital", 78), ("sita", 90), ("Nita", 76)] 
d={} 
threshold=80 
s=set() 
for t in l: 
    d[t[0]]=t[1] 
for k,v in d.items(): 
    if v>threshold: 
     s.add(k) 
print(s) 