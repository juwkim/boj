K, P, X = map(int, input().split())
M = int((K*P/X)**.5)
print('%.3f' % min(X*M+K*P/M, X*(M+1)+K*P/(M+1)))