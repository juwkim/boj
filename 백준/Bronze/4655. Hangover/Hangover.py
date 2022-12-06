while True:
    c = float(input())
    if c == 0.0:
        break
    i = 2
    total = 0
    while total < c:
        total += 1/i
        i += 1
    print(f'{i-2} card(s)')