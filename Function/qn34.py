#34.Use a lambda function with map() to convert a list of temperatures from Celsius to Fahrenheit.

celsius_lst=[32,33,34,35,36,37,38,39,40]
fahrenheit_lst=list(map(lambda x:(x*9/5)+32,celsius_lst))
print(fahrenheit_lst)