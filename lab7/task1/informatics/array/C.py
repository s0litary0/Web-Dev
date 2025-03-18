n = int(input())  
arr = list(map(int, input().split())) 

exists = any(arr[i] * arr[i - 1] > 0 for i in range(1, n))
print("YES" if exists else "NO")
