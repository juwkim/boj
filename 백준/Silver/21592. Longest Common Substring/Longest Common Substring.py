from sys import exit
N = int(input())
buf = [input() for _ in range(N)]
buf.sort(key=len)
Min = buf.pop(0)

for l in range(len(Min), -1, -1):
    for s in range(len(Min)-l+1):
        if all(Min[s:s+l] in line for line in buf):
            print(l)
            exit(0)