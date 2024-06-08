
import sys
input = lambda: sys.stdin.readline().strip()

def solve():
    n = int(input())
    buf = [0] * n
    i = 0
    while i < n:
        s = input()
        if s == 'T':
            j = i - 1
            while j and buf[j - 1] != buf[i - 1]:
                j -= 1            
            visited = bytearray(100)
            cycle = []
            while j < i:
                if not visited[buf[j]]:
                    cycle.append(buf[j])
                    visited[buf[j]] = True
                j += 1
            idx = 0
            while s == 'T':
                buf[i] = cycle[idx]
                print(buf[i])
                idx = (idx + 1) % len(cycle)
                i += 1
                if i == n: return
                s = input()
        buf[i] = int(s)
        i += 1
solve()