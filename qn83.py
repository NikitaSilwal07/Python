import random
for i in range(4,0,-1):
    for j in range(i):
        print(random.randint(0,9),end="")
    print()
