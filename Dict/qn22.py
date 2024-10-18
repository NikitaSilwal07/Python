#22. How do you count the occurrences of each element in a list using a dictionary?

l=[1,11,10,20,30,40,50,40,10,50,40,3,11,50,60,30,50,10,50,20,10,10,1,10] 
count_dic={} 
for items in l: 
    if items in count_dic: 
       count_dic[items]=count_dic[items]+1 
    else: 
        count_dic[items]=1

print(count_dic) 