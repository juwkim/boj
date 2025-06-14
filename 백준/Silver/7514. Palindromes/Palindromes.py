import sys
input = sys.stdin.readline

def to_base(x, b):
    digits = []
    while True:
        digits.append("0123456789abcdefghijklmnopqrstuvwxyz"[x % b])
        x //= b
        if x == 0:
            break
    return ''.join(reversed(digits))

for tc in range(1, int(input()) + 1):
    b, l = map(int, input().split())
    s, e = map(lambda x: int(x, b), input().split())
    cnt = 0
    for n in range(s, e + 1):
        cur = n
        for _ in range(l + 1):
            num = to_base(cur, b)
            if num == num[::-1]:
                break
            cur += int(num[::-1], b)
        else:
            cnt += 1
    print(f"Scenario {tc}:\n{cnt}")