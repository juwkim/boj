import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]


while n:= int(input()):
    dic = {}
    for _ in range(n):
        item, *l = input().split()
        l = [*map(int, l)]
        dic[item] = l
    
    ans = 0
    for _ in range(int(input())):
        cost = 0
        num, P, M = g()
        flag = True
        for _ in range(P):
            val, due = dic[input()]
            if due <= M:
                cost += val
            else:
                flag = False
        if flag:
            print(num, cost)
        else:
            print(num, cost, '*')
            ans += 1
    print('Number of discontented customers is:', ans)