for _ in range(int(input())):
    score = 0
    before = 0
    cnt = 0
    for i in input():
        if '0' <= i <= '9':
            score += int(i)
        else:
            score += ord(i) - 55
        if score >= 40:
            break
        a = score // 10
        if a > before:
            cnt += a
            before = a
    if score >= 50:
        print(f'{cnt}(09)')
    elif score >= 40:
        print(f'{cnt}(weapon)')
    else:
        print(cnt)