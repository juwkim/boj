for day in range(1, 1 + int(input())):
    c, d = map(int, input().split())
    ans, idx = 0, 0
    line = input()
    while idx != c - 1:
        Next = min(idx + d + 1, c - 1)
        while Next != idx and line[Next] == 'X':
            Next -= 1
        if Next == idx:
            ans = 0
            break
        ans += 1
        idx = Next
    print(f'Day #{day}\n{c} {d}\n{line}\n{ans}\n')