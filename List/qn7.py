#7. How can you concatenate two lists?
l1 = [10,20,30]
l2 = ["hello", 10.5,90]
l1.extend(l2)
print(l1)

#OR
l1 = [10,20,30]
l2 = ["hello", 10.5,90]
print(l1 + l2)