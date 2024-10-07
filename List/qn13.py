#13. How do you check if a list is empty?
l1=[]
if not l1:
    print("The list l1 is empty")
else:
    print("The list l1 not  empty")

    #OR
l1=[10,20,30,"hello",40.5]
if len(l1) == 0:
    print("The list is empty")
else:
    print("The list is not empty")

