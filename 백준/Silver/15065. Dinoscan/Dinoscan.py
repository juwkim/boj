def solve():
    r, c1, c2 = map(int, input().split())
    bone1 = [list(input()) for _ in range(r)]
    bone2 = [list(input()) for _ in range(r)]
    for l in range(1, c1 + c2 + 1):
        if any(bone[i] != '0' for bone in bone1 for i in range(l, c1)):
            continue
        if any(bone[i] != '0' for bone in bone2 for i in range(c2 - l)):
            continue
        success = True
        for p, q in zip(bone1, bone2):
            board = ['0' for _ in range(l)]
            board[:min(c1, l)] = p[:min(c1, l)]
            for j in range(min(c2, l)):
                a, b = board[l - 1 - j], q[c2 - 1 - j]
                if a + b == "11":
                    success = False
                    break
                elif a + b == "01":
                    board[l - 1 - j] = '1'
            if not success or any(c == '0' for c in board):
                success = False
                break
        if success:
            return "Yes"
    return "No"
print(solve())