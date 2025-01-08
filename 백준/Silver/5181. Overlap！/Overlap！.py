import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    m, n = map(int, input().split())
    off = {'M': 0, 'T': 1440, 'W': 2880, 'TH': 4320, 'F': 5760}
    d = {}
    for _ in range(m):
        course, day, time = input().split()
        s, e = time.split('-')
        h1, m1 = map(int, s.split(':'))
        h2, m2 = map(int, e.split(':'))
        start = off[day] + h1 * 60 + m1
        end = off[day] + h2 * 60 + m2
        d[course] = start, end
    ans = 0
    for _ in range(n):
        course = sorted(input().split(), key=lambda x: d[x][1])
        if any(d[course[i]][0] < d[course[i - 1]][1] for i in range(1, len(course))):
            ans += 1
    print(f"Data Set {tc}:\n{ans}")