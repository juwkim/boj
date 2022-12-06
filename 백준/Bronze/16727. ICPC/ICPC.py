import sys
p1, s1, s2, p2 = map(int, sys.stdin.read().split())
p, s = p1 + p2, s1 + s2
ans = ['Persepolis', 'Esteghlal']
print([ans[p < s],[ans[p2 < s1] ,'Penalty'][p2 == s1]][p == s])