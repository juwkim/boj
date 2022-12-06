N, P, S = map(int, input().split())
for _ in range(S):
    print(['REMOVE', 'KEEP'][P in map(int, input().split()[1:])])    