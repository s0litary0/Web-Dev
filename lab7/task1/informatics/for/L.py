x = input()

res = 0
power = 0
for i in reversed(x):
    res += int(i) * 2 ** power
    power += 1

print(res)
