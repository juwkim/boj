for i in range(1, 1 + int(input())):
    n, p, q = map(int, input().split())
    weight, cnt = 0, 0
    for num in sorted(map(int, input().split())):
        weight += num
        if weight > q:
            break
        cnt += 1
        if cnt == p:
            break
    print(f'Case {i}: {cnt}')