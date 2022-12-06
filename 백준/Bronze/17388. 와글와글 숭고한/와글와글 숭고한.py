A = list(map(int, input().split()))
print('OK' if sum(A) >= 100 else ['Soongsil', 'Korea', 'Hanyang'][A.index(min(A))])