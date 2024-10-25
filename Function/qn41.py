#41.Write a function find_max_in_args(*args) that returns the maximum value from the arguments passed.

def find_max_in_args(*args):
 if args:
     maximum=args[0]
 else:
    return False
 for x in args:
     if x>maximum:
        maximum=x
 return maximum
max_value= find_max_in_args()
if max_value:
 print("The maximum is:",max_value)
else:
 print("No value passed.")