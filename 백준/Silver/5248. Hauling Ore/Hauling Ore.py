from collections import defaultdict

def solve(start_idx):
    adj = defaultdict(set)
    i = start_idx + 1
    while i < len(lines) and lines[i] != "GRAPH END":
        parts = lines[i].split()
        u = parts[0]
        for v in parts[1:]:
            adj[u].add(v)
            adj[v].add(u)
        i += 1
    i += 1
    while i < len(lines) and lines[i] != "GRAPH BEGIN":
        u = lines[i]
        if u in adj:
            reach = set()
            for w in adj[u]:
                reach |= adj[w]
            print(*sorted(reach - {u} - adj[u]))
        else:
            print(u)
        i += 1
    return i

lines = [*map(str.strip, open(0))]
idx = 0
while idx < len(lines):
    idx = solve(idx)