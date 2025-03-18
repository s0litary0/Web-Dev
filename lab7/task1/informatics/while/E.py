n = int(input())

res = 1
power = 0
while True:
    if res > n:
        print(power)
        break
    else:
        power += 1
        res *= 2