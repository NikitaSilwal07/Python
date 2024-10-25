#31.Write a lambda function to filter even numbers from a list.

l=[x for x in range(0,50)]
even_list=list(filter(lambda x:x%2==0,l))
print(even_list)