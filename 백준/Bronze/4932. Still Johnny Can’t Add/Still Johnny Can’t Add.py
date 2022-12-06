g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    n = int(input())
    nums = [g() for _ in range(n)]
    ans = 'YES'
    for j in range(n-1):
        if len({l[j+1] - l[j] for l in nums}) == 1:
            continue
        else:
            ans = 'NO'
            break
    print(f'{cnt}. {ans}')