# 21. Write a program that splits a string by commas and then sorts each word in alphabetical order.

input_string = "python, is, fun."
split_string=input_string.split(", ")
print(split_string)
sorted_word_in_list=sorted(split_string)
print(sorted_word_in_list)
sorted_word=" ".join(sorted_word_in_list)
print(sorted_word)