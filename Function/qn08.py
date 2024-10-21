#8. Write a function count_vowels(s) that returns the number of vowels in the string s.

def count_vowels(s): 
    vowels=['a','e','i','o','u'] 
    count=0 
    for x in s: 
       if x.lower() in vowels: 
          count+=1 

    return count 
user_input=input("Enter a string : ") 
print(f"The number of vowel in {user_input} is : {count_vowels(user_input)}")
