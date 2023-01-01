def g(): return map(int, input().split())

for _ in range(int(input())):
    N = int(input())
    
    cur = 1
    stack = []
    for num in g():
        if cur == num:
            cur += 1
        else:
            while stack and cur == stack[-1]:
                stack.pop()
                cur += 1
            stack.append(num)

    while stack and cur == stack[-1]:
        stack.pop()
        cur += 1

    if cur == N + 1:
        ans = 'yes'
    else:
        ans = 'no'
    print(ans)