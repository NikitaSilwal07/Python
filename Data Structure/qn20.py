#20. List & Dic onary: Given a list of students with their names and grades (e.g., ("John", 85)), 
# return a dictionary where the keys are the grades and the values are lists of students 
# who received that grade.

l=[(100,"Nikita"),(67,"Archana"),("Isha",67),("anmol",90),("Bibek",35)]
d={} 
for t in l: 
    if t[1] in d: 
      d[t[1]].append(t[0]) 
    else: 
      d[t[1]]=[t[0]] 
print(d) 