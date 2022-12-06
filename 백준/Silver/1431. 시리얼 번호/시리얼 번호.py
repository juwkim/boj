def check(x):
    
    ans = 0
    for i in x:
        if i.isnumeric():
            ans += int(i)
    
    return ans

buf = [input() for _ in range(int(input()))]
buf.sort(key=lambda x: (len(x), check(x), x))
print(*buf)