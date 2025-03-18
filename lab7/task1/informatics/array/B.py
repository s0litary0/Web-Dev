n = int(input()) 
arr = list(map(int, input().split())) 

even_numbers = [num for num in arr if num % 2 == 0]
print(*even_numbers)