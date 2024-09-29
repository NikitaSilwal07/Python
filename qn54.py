n = 9
for i in range(1, n + 1):
    if i == n:
        print('*' * n)
    else:
        print('*' + ' ' * (i - 1) + ('*' if i > 1 else ''))
