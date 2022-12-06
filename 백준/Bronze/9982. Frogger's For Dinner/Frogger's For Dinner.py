g = lambda: [*map(int, input().split())]

while True:
    try:
        input()
        safecolumn = [True] * 10
        for r in range(1, 9):
            d = [-1, 1][r > 4]            
            nums = g()
            
            for c in range(10):
                v = nums[c]
                if v == 0:
                    continue
                idx = (r - 1) * v * d + c
                for i in range(v+1):
                    safecolumn[idx % 10] = False
                    idx += d
        if any(safecolumn):
            print("LEFTOVER POSSUM")
        else:
            print("FROGGER")
        input()
    except:
        break