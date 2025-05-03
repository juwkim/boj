import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    queries = []
    for _ in range(M):
        bits, cnt = input().split()
        queries.append((bits, int(cnt)))
    valid_state = None
    for state in map(lambda x: bin(x)[2:].zfill(N), range(1 << N)):
        if all(q_cnt == sum(q_bin[i] + state[i] == '11' for i in range(N)) for q_bin, q_cnt in queries):
            if valid_state:
                return "NOT UNIQUE"
            valid_state = state
    if valid_state is None:
        return "IMPOSSIBLE"
    return valid_state
print(solve())