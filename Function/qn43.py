#43.Write a recursive function flatten_recursive(*args) that flattens any number
#  of nested lists passed as arguments.

def sum_all_recursive(*args):
    sum=0
    for items in args:
        if isinstance(items,tuple) or isinstance(items,list):
         sum=sum+sum_all_recursive(*items)
        else:
            sum=sum+items
    return sum

print(f"The sum is: {sum_all_recursive(10,9,[6,(3,4,5),9,[8,5,3]],(3,[5,3,[1,2,3]]))}")