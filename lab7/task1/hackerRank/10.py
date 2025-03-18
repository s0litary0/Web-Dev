students = [[input(), float(input())] for _ in range(int(input()))]

second_lowest = sorted(set(score for name, score in students))[1]

print("\n".join(sorted(name for name, score in students if score == second_lowest)))
