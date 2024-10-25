#37.Write a function print_details(**kwargs) that prints out all the key-value pairs passed 
# as keyword arguments.

def print_details(**kwargs):
 for k,v in kwargs.items():
     print(f"{k}:{v}")
 
print_details(a=10,b=20,c=4)