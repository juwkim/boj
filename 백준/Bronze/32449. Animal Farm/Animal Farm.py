import sys
input = sys.stdin.readline

ans = 0
influences = []
for _ in range(int(input())):
    species, influence = input().split()
    influence = int(influence)
    if species == 'pig':
        ans = max(ans, influence)
    else:
        influences.append(influence)
ans += sum(influence for influence in influences if influence < ans)
print(ans)