# class A:
#  """This class is demo class.This class does nothing"""
#  #attributes
#  #behavior
# print(A.__doc__)

# class A:
#  pass

#Class creation
class student:
 """This is creation of class."""
def __init__(self):
    self.name="Nikita"
    self.roll="49"
    self.marks=98
def talk(self):
 print(f'Hello My name is : {self.name}')
 print(f'Hello My marks is : {self.marks}')
#Object creation
s=student()
print(s.name)
print(s.marks)
s.talk()