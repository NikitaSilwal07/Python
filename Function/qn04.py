#4. Write a function find_max(a, b, c) that returns the largest of three numbers.

def find_max(a,b,c): 
    if a>b and a>c: 
      return a 
    elif b>c: 
       return b 
    else: 
        return c 
    
largest=find_max(10,20,15)
print(largest)