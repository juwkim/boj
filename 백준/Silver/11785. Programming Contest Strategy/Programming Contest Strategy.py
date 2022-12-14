g = lambda: map(int, input().split())
for i in range(1, 1 + int(input())):
    N, L = g()
    solved, cur, total = 0, 0, 0
    for num in sorted(g()):
        if cur + num > L:
            break
        solved += 1
        cur += num
        total += cur
    print(f'Case {i}:', solved, cur, total)