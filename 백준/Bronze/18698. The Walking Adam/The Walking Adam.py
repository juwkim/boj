for _ in range(int(input())):
    s = input()
    ans = s.find('D')
    print(ans if ans != -1 else len(s))