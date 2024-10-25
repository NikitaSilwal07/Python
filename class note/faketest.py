# from random import * 
 
# alphabets='abcdefghijklmnopqrstuvwxyz' 
# digits='0123456789' 
# cities=['Kathmandu','Pokhara','Biratnagar','Kavre','Dolakha','Butwal','Hetauda'] 
# designation=['Software Engineer','Sr. Software engineer','Team Lead','Project Lead','Manager'] 
 
# def get_fake_name(): 
#     name = choice(alphabets).upper() 
#     n=randint(2,9) 
#     for i in range(n): 
#         name = name + choice(alphabets) 
#     return name 
 
# def get_fake_employee_num(): 
#     enum= 'e-' 
#     for i in range(4): 
#         enum = enum + choice(digits) 
#     return enum 
 
# def get_fake_salary(): 
#     esal = uniform(10000,50000) 
#     return esal 
 
# def get_fake_city(): 
#     city=choice(cities) 
#     return city 
 
# def get_fake_mobile_number(): 
#     mobile_number= '9' 
#     for i  in range(9): 
#         mobile_number=mobile_number+choice(digits) 
#     return mobile_number 
 
# def get_fake_designation(): 
#     desig=choice(designation) 
#     return desig

# print("Employee records:") 
# print("Name :",get_fake_name()) 
# print("Employee number :",get_fake_employee_num()) 
# print("Salary : {:.2f}".format(get_fake_salary())) 
# print("Mobile number :",get_fake_mobile_number()) 
# print("City :",get_fake_city()) 
# print("Designation :",get_fake_designation()) 