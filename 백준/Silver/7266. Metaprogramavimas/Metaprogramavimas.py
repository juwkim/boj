import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    l = [[*map(int, input().split())] for _ in range(N)]
    dic = {}
    for a, b in l:
        if a in dic and dic[a] != b:
            return -1
        dic[a] = b
    nums = list(dic.items())
    if all(a == b for a, b in nums):
        return "1\nprint"
    a, b = nums[0]
    if a <= b and all(b - a == y - x for x, y in nums):
        return f"2\nadd {b - a}\nprint"
    s, good = set(), True
    for x, y in nums:
        if (x, y) == (0, 0):
            continue
        if x == 0:
            good = False
            break
        q, r = divmod(y, x)
        if r:
            good = False
            break
        s.add(q)
    if good and len(s) == 1:
        return f"2\nmultiply {s.pop()}\nprint"
    if len(nums) == 1:
        return f"3\nmultiply 0\nadd {b}\nprint"
    (x1, y1), (x2, y2) = nums[:2]
    if any((x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1) for x3, y3 in nums[2:]):
        return -1
    num1, r = divmod(y2 - y1, x2 - x1)
    num2 = y1 - num1 * x1
    if r or num1 < 0 or num2 < 0:
        return -1
    return f"3\nmultiply {num1}\nadd {num2}\nprint"

print(solve())