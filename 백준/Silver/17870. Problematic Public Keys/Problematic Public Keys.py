ans = set()
for _ in range(int(input())):
    num = int(input())
    
    div = 2
    while num % div:
        div += 1
    ans.add(div)
    ans.add(num // div)
ans = sorted(ans)

for i in range(0, len(ans), 5):
    print(*ans[i:i+5])