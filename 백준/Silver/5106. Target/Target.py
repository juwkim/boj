while N:= int(input()):
    left = set(chr(i) for i in range(97, 123))
    for _ in range(N):
        word = input()
        left &= set(word)
        if len(word) == 9:
            total = word
    left = left.pop()
    ans = sorted(total)
    ans.remove(left)
    ans.insert(4, left)
    print(*map(str.upper, ans))