def base_start(l):
    c = max(l)
    if c.isdigit():
        return max(2, int(c) + 1)
    return ord(c) - 86

def solve():
    S, T = input().split()
    ans = "Impossible"
    for i in range(base_start(S), 37):
        for j in range(base_start(T), 37):
            if i != j and int(S, i) == int(T, j):
                if ans[0] != 'I':
                    return "Multiple"
                ans = f"{int(S, i)} {i} {j}"
    return ans
print(solve())