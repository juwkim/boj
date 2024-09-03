s, prev = set([0]), 0
for i in range(1, int(input()) + 1):
    num = prev - i
    if num < 0 or num in s:
        num = prev + i
    s.add(num)
    prev = num
print(prev)