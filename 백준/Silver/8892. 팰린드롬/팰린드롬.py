import sys
input = lambda: sys.stdin.readline().rstrip('\n')

for _ in range(int(input())):
    k = int(input())
    ans = 0
    words = [input() for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if i != j:
                tmp = words[i] + words[j]
                if tmp == tmp[::-1]:
                    ans = tmp
                    break
    print(ans)