count = 0
for _ in range(int(input())):
    a, b, c, d = map(float, input().split())
    if (a+b+c <= 125 or (a <= 56 and b <= 45 and c <= 25)) and d <= 7:
        count += 1
        print(1)
    else:
        print(0)
print(count)