#27.Write a recursive function flatten(lst) that flattens a nested list structure.

def flatten(lst):
     l=[]
     for item in lst:
        if isinstance(item,list):
            l.extend(flatten(item))
        else:
             l.append(item)
     return l
lst=[1,["Nikita","Silwal",["Bhaktapur"],[58,88]],["Across","Himalayan"],59,15]
print(flatten(lst))