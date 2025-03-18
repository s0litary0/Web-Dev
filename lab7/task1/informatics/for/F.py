x = input()

for i in reversed(x):
    if i == '0':
        continue
    print(i, end="")