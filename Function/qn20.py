#20.Write a function is_anagram(s1, s2) that checks if two strings s1 and s2 are anagrams of each other.

def is_anagram(s1,s2):
    if len(s1)!=len(s2):
       return False
    if sorted(s1)==sorted(s2):
      return True
    else:
       return False
s1="silent"
s2="listen"
if is_anagram(s1,s2):
 print(f"{s1} and {s2} are anagram.")
else:
 print(f"{s1} and {s2} are not anagram.")