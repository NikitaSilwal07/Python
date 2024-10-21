#9. Write a function is_prime(n) that checks if a number n is prime.

def is_prime(n): 
     count=0 
     for i in range(2,n): 
        if n%i==0: 
          count+=1 
        if count == 0: 
           return True 
        else: 
            return False 
a=99
if is_prime(a): 
   print(f"{a} is prime number.") 
else: 
    print(f"{a} is not prime number.") 