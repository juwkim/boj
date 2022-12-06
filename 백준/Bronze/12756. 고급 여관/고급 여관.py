A, B = map(int, input().split())
C, D = map(int, input().split())
print('DRAW' if -D//A == -B//C else ['PLAYER A', 'PLAYER B'][-D//A < -B//C])