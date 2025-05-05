import sys
input = sys.stdin.readline

while n:=int(input()):
    mat = [[*map(int, input().split())] for _ in range(n)]
    row_sum = [sum(row) & 1 for row in mat]
    col_sum = [sum(mat[i][j] for i in range(n)) & 1 for j in range(n)]
    odd_rows = [i for i in range(n) if row_sum[i]]
    odd_cols = [j for j in range(n) if col_sum[j]]
    if not odd_rows and not odd_cols:
        print("OK")
    elif len(odd_rows) == 1 and len(odd_cols) == 1:
        print(f"Change bit ({odd_rows[0] + 1},{odd_cols[0] + 1})")
    else:
        print("Corrupt")