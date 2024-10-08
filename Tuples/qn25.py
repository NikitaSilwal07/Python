#25.How can you use a generator to create a tuple?
t=(x for x in range(1,30) if x%3==0) 
print(tuple(t)) 