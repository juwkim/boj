g = lambda: [*map(int,input().split())]

king = g()
ans, best = -1, [1, 1, 1]
def compare(day1, day2):
    d1, m1, y1 = day1
    d2, m2, y2 = day2
    if y1 != y2:
        return (y1 > y2) - (y1 < y2)
    elif m1 != m2:
        return (m1 > m2) - (m1 < m2)
    else:
        return (d1 > d2) - (d1 < d2)


for i in range(1, 1 + int(input())):
    prince = g()
    prince[2] += 18
    if compare(king, prince) >= 0 and compare(best, prince) < 0:
        best = prince
        ans = i
print(ans)