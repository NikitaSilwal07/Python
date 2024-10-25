#42.Write a recursive function sum_all_recursive(*args) that sums all numbers passed as arguments
#  (including nested tuples or lists).

def find_max_in_args(*args):
 if args:
     maximum=args[0]
 else:
     return False
 for x in args:
    if x>maximum:
        maximum=x
 return maximum
max_value= find_max_in_args(6,9,10,42,3,4,5,1)
if max_value:
 print("The maximum is:",max_value)
else:
 print("No value passed.")