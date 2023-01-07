from collections import deque

for _ in range(int(input())):
    
    input()
    B, five = deque(), 0
    ans = []
    for _ in range(int(input())):
        if B and five:
            B.popleft()
            five -= 1

        name, money = input().split()
        money = int(money)
        
        if money == 15:
            five += 1
        elif five:
            five -= 1
        else:
            B.append(name)
        
        if len(B) > len(ans):
            ans = list(B)
    
    if ans:
        print(*ans)
    else:
        print('Line B stayed empty.')