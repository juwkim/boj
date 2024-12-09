import sys
input = sys.stdin.readline

def up(num):
    cnt = 0
    while num != C and num <= 146000:
        cnt += 1
        num += 20
    if num == C:
        return cnt
    num = 144000
    while num != C and num <= 146000:
        cnt += 1
        num += 20
    if num == C:
        return cnt
    return 1e9

def down(num):
    cnt = 0
    while num != C and num >= 144000:
        cnt += 1
        num -= 20
    if num == C:
        return cnt
    num = 146000
    while num != C and num >= 144000:
        cnt += 1
        num -= 20
    if num == C:
        return cnt
    return 1e9

for _ in range(int(input())):
    A, B, cur, C = input().split()
    A, B, C = float(A) * 1000, float(B) * 1000, float(C) * 1000
    ans = min(6, up(A) + (cur == 'B'), up(B) + (cur == 'A'))
    ans = min(ans, down(A) + (cur == 'B'), down(B) + (cur == 'A'))
    print(ans)