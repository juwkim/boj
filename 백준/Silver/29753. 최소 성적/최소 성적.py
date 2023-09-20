import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

dic = {"A+": 450, "A0": 400, "B+": 350, "B0": 300,
    "C+": 250, "C0": 200, "D+": 150, "D0": 100, "F": 0
}
ans = "impossible"
N, X = input().split()
a, b = map(int, X.split('.'))
X = a * 100 + b
credit, grade = 0, 0
for _ in range(int(N) - 1):
    c, g = input().split()
    c = int(c)
    credit += c
    grade += c * dic[g]

L = int(input())
credit += L
for k, v in sorted(dic.items(), reverse=True):
    score = (grade + v * L) // credit
    if score > X:
        ans = k
        break
print(ans)