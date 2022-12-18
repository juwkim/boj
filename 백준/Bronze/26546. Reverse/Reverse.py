for _ in range(int(input())):
    s, *l = input().split()
    i, j = map(int, l)
    print(s[:i] + s[j:])