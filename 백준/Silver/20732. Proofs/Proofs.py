check = set()
ans = 'correct'
for i in range(1, int(input()) + 1):
    *assumptions, arrow, conclusion = input().split()
    if assumptions and any(assumption not in check for assumption in assumptions):
        ans = i
        break
    check.add(conclusion)
print(ans)