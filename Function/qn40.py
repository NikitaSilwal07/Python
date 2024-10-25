#

def combine_args_kwargs(*args, **kwargs):
 print("The elements in args are : ")
 for x in args:
    print (x)
 print("The key in kwargs are : ")
 for key,value in kwargs.items():
    print (f'{key}')
combine_args_kwargs(5,9,10,22,key="Jaya",Dentist="Osho")