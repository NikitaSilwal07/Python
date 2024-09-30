list=["",'A','B','C','D']
for i in range(4,0,-1):
    number=1 if i%2==0 else 3
    for j in range(i):
        print(list[number],end="")
        number=number+1
        if number>4:
            number=number%4
    print()

# def print_char_pyramid():
#     # Define the base string (starting characters)
#     base_str = 'ABCD'
#     length = len(base_str)
    
#     for i in range(length, 0, -1):
#         # For each row, slice and concatenate the parts accordingly
#         if i % 2 == 0:
#             print(base_str[:i])  # Even rows, print from start
#         else:
#             print(base_str[-i:])  # Odd rows, print from end

# print_char_pyramid()

