#20.How do you check if a tuple contains other tuples as elements?

tuples_of_tuple=(3,4,5,0,9,7,0x123,"By") 
for items in tuples_of_tuple: 
    if isinstance(items,tuple): 
        print("It contains tuple as another element.") 
        break 
else: 
    print("It does not contain another tuple as element.") 