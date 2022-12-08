import sys
input = lambda: sys.stdin.readline().rstrip()
dic = {'S': 'SML', 'M': 'ML', 'L': 'L'}
J = int(input())
A = int(input())
clothes = [input() for _ in range(J)]
ans = 0
for _ in range(A):
    size, num = input().split()
    num = int(num) - 1
    if clothes[num] in dic[size]:
        ans += 1
        clothes[num] = '-'
print(ans)