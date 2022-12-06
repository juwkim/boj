def sieve(N):
    check = [False, False] + [True] * (N - 1)
    for i in range(2, int(N**.5) + 1):
        if check[i]:
            for j in range(2*i, N+1, i):
                check[j] = False
        
    primes = list(filter(lambda x: check[x], range(2, N+1)))
    return primes

N = int(input())
K = int(input())

primes = sieve(min(N, K))
l = len(primes)
cnt = 1
def solve(num, idx):
    global cnt
    if idx >= l:
        return
    solve(num, idx+1)
    
    num *= primes[idx]
    if num > N:
        return
    cnt += 1
    solve(num, idx)
solve(1, 0)
print(cnt)