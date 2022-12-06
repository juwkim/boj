b, w = sorted(map(int, input().split()))
if b == w == 0:
    print("Impossible")
else:
    num = 0
    step, count = 2, 0
    i = 1
    while num + step <= b:
        num += step
        count += 1
        i += 1
        if count == 2:
            count = 0
            step += 2
    if w == num and i % 2:
        i -= 1
    print(i)