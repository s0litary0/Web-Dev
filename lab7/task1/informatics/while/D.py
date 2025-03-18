n = int(input())

i = 0
res = 1
while i < n:
    if res == n:
        print("YES")
        break
    else:
        res *= 2
        i += 1
else:
    print("NO")