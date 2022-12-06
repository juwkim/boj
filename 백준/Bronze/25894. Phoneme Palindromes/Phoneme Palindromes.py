for i in range(1, 1 + int(input())):
    print("Test case #%d:" % i)
    dic = {chr(i): chr(i) for i in range(97, 123)}
    for _ in range(int(input())):
        a, b = input().split()
        dic[a] = b
    for _ in range(int(input())):
        s = input()
        buf = [dic[c] for c in s]
        ans = 'NO'
        if buf == buf[::-1]:
            ans = 'YES'
        print(s, ans)
    print()