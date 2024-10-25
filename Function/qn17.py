#17.Write a function longest_word(words) that returns the longest word from a list of words.

def longest_word(words):
    longest=words[0]
    for word in words:
      if len(word)>len(longest):
        longest=word
    return longest
l=["Python","Programming","is","always","entertaining","and","enjoyable."]
print("The longest word in list of words is",longest_word(l)) 