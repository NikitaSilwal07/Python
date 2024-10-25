#32.Write a lambda function that finds the maximum of two numbers.

user_input1 = int (input ("Enter a number : "))
user_input2 = int (input ("Enter another number : "))

greatest=lambda user_input1,user_input2:user_input1 if user_input1>user_input2  else user_input2
print(f"Greatest number of {user_input1} and {user_input2} is {greatest(user_input2,user_input1)}")