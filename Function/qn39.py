#39.Write a function describe_person(name, **kwargs) where name is a required argument,
#  and other details like age, job, and city are optional keyword arguments.

def describe_person(name, **kwargs):
 print(f"Details of student {name} is : ")
 for k,v in kwargs.items():
      print(f'{k}:{v}')
 return None
describe_person('Nikita',age=21,city="Kathmandu")