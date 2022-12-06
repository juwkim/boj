from collections import*
N,d=int(input()),deque()
exec("d.appendleft(N);d.rotate(N);N-=1;"*N)
print(*d)