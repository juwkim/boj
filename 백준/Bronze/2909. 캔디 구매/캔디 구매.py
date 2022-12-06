C,K=map(int,input().split())
if C % 10**K >= 10**K / 2:
    print((C // 10**K + 1) * 10**K)
else:
    print(C // 10**K * 10**K)