n, m = map(int, input().split())
x = sorted([*map(int, input().split())], reverse=True)
y = sorted([*map(int, input().split())], reverse=True)
A_count, B_count = 1, 0

while y:
    if B_count:
        A_count += y.pop(0)
        B_count -= 1
    elif A_count and x:
        B_count += x.pop(0)
        A_count -= 1
    else:
        break

print(A_count)