number=9
for i in range(5):
    for j in range(i+1):
        print(number,end=" ")
        number=number-2
    print()
    if i==0:
      number=number+1
    else:
        number=number+3
    if number<0:
        number*=-1