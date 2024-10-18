#26. How do you use a dictionary to simulate a switch-case statement?

# For all days 
# for k,v in d1.items(): 
# print(f"For {k}, it is {v}") 
# For specific case:

d1 = {

    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday",
} 
user_input=int(input("Enter a number of day of week: ")) 
print(f"{user_input} is {d1.get(user_input,"Invalid day")}") 