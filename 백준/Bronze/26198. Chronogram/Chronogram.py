dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
for _ in range(int(input())):
    ans = 0
    for s in input():
        if s in dic:
            ans += dic[s]
    print(ans)