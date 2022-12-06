for _ in range(int(input())):
    s = sorted([i for i in input().lower() if i.isalpha()])
    if len(s) % 2 == 0 and all(ord(s[i]) + ord(s[len(s) - 1 - i]) == 219 for i in range(len(s)//2)):
        print('Yes')
    else:
        print('No')