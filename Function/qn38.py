#38.Write a function concatenate_strings(*args) that concatenates an arbitrary number of strings.

def concatenate_strings(*args):
 string=''
 for x in args:
   string+=x
 return string
print(concatenate_strings("Nikita ","love","playing","Basketball."))