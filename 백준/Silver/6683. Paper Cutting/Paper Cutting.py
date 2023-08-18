def get_count(r, c, row, col):
    if r > row or c > col:
        return float("inf")
    cnt = A * B - 1
    if row > r:
        cnt += 1
    if col > c:
        cnt += 1
    return cnt

while True:
    A, B, C, D, E, F = map(int, input().split())
    if A == 0:
        break
    cnt = min(get_count(A * C, B * D, E, F),
              get_count(A * D, B * C, E, F),
              get_count(A * C, B * D, F, E),
              get_count(A * D, B * C, F, E))
    if cnt == float("inf"):
        print("The paper is too small.")
    else:
        print(f"The minimum number of cuts is {cnt}.")