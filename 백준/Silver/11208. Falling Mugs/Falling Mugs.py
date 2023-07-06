ans = "impossible"
n1, n2 = 0, 1
D = int(input())
while n1 != n2:
    diff = n2 * n2 - n1 * n1
    if diff == D:
        ans = f"{n1} {n2}"
        break
    elif diff > D:
        n1 += 1
    else:
        n2 += 1
print(ans)