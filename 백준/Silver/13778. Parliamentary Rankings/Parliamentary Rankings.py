import sys
input = lambda: sys.stdin.readline().rstrip()

name, score = {}, {}
for _ in range(int(input())):
    I, *M = input().split()
    I, M = int(I), " ".join(M)
    name[I], score[I] = M, 0
dic = {'S': 10, 'Q': 5, 'A': 7, 'L': -8, 'F': 4, 'D': -5, 'E': -10}
for _ in range(int(input())):
    I, code = input().split()
    score[int(I)] += dic[code]
Max, Min = max(score.values()), min(score.values())
l_Max = [name[k] for k in sorted(name) if score[k] == Max]
l_Min = [name[k] for k in sorted(name) if score[k] == Min]
print(Max, *l_Max)
print(Min, *l_Min)