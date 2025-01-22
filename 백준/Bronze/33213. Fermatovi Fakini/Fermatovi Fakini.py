import sys
input = sys.stdin.readline

odd, even = set(), set()
input()
for num in map(int, input().split()):
    if num & 1:
        odd.add(num)
    else:
        even.add(num)
if len(odd) > len(even):
    ans = 1
    while ans in odd:
        ans += 2
else:
    ans = 2
    while ans in even:
        ans += 2
print(ans)