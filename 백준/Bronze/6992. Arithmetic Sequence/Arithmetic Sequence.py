for _ in range(int(input())):
    a = [*map(int, input().split())][1:]
    if len(set([x - y for x, y in zip(a, a[1:])])) == 1:
        five = [a[-1] + i * (a[1] - a[0]) for i in range(1, 6)]
        print(f'The next 5 numbers after {a} are: {five}')
    else:
        print(f'The sequence {a} is not an arithmetic sequence.')