#22. How would you check if a list is a palindrome?
l=[10,20,30,40,50,60,70,80,90,10] 
if l==l[::-1]: 
  print("List is palindrome.") 
else: 
  print("List is not palindrome.") 


l=[1, 2, 3, 4, 5, 6,6, 5,4,3,2,1] 
if l==l[::-1]: 
   print("List is palindrome.") 
else: 
    print("List is not palindrome.") 