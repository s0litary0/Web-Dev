n = int(input())

array = []
for _ in range(n):
    array.append(int(input))

for i in array[::2]:
    print(i, end=" ")
