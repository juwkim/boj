import sys
input = sys.stdin.readline

STEP = 43200
for tc in range(1, 1 + int(input())):
    a, typ, b = input().split()
    a, b = int(a), int(b)
    k = (11 * (b % 12 * 3600) - 120 * a + (-1, STEP)[typ == 'after']) // STEP * STEP
    sec = (2 * (120 * a + k) + 11) // 22 % STEP
    h = (sec // 3600 - 1) % 12 + 1
    m, s = divmod(sec % 3600, 60)
    print(f"Case {tc}: {h}:{m:02d}:{s:02d}")