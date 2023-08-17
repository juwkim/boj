t = 0
for _ in range(int(input())):
    m, s = map(int, input().split(':'))
    t += m * 60 + s

h, m, s = t // 3600, (t % 3600) // 60, t % 60
print(f"{h:02d}:{m:02d}:{s:02d}")