while (n := int(input())):
    for _ in range(n):
        a = [idx for idx, num in enumerate(input().split()) if int(num) <= 127]
        print(chr(ord('A') + a[0]) if len(a) == 1 else '*')