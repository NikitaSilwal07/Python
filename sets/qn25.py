#25.How do you remove multiple elements from a set at once?

s1={10,20,30,40,50,"nikita",55.5}
s1.difference_update({10,30,55.5})
print(s1)