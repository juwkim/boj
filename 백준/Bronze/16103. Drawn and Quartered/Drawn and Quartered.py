N, K = map(int, input().split())
a = input()
s = [a[i:i+N//4] for i in range(0, N, N//4)]
if K%3 == 0:
    print(a)
elif K%3 == 1:
    print(s[0]+s[3]+s[1]+s[2])
else:
    print(s[0]+s[2]+s[3]+s[1])