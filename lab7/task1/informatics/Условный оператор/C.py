number = int(input())

answer = int(input())

real_answer = 1 if (
    number // 1000 == number % 10 and
    number // 100 - number // 1000 * 10 == number % 100 // 10
) else -1

print("YES" if real_answer == answer
else "NO")

print(
    ( number // 1000, number % 10 ),
    ( number // 100 - number // 1000 * 10, number % 100 // 10 )
)