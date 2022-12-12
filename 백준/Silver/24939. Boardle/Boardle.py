g = lambda: map(int, input().split())

N, M = g()
nLow, mLow, nHigh, mHigh = 1, 1, N, M
for _ in range(int(input())):
    x, y, d = g()
    if d == 1:
        nLow, mLow, nHigh, mHigh = max(nLow, x + 1), y, nHigh, y
    elif d == 2:
        nLow, mLow, nHigh, mHigh = nLow, y, min(nHigh, x - 1), y
    elif d == 3:
        nLow, mLow, nHigh, mHigh = x, mLow, x, min(mHigh, y - 1)
    elif d == 4:
        nLow, mLow, nHigh, mHigh = x, max(mLow, y + 1), x, mHigh
    elif d == 5:
        nLow, mLow, nHigh, mHigh = max(nLow, x + 1), max(mLow, y + 1), nHigh, mHigh
    elif d == 6:
        nLow, mLow, nHigh, mHigh = nLow, max(mLow, y + 1), min(nHigh, x - 1), mHigh
    elif d == 7:
        nLow, mLow, nHigh, mHigh = max(nLow, x + 1), mLow, nHigh, min(mHigh, y - 1)
    elif d == 8:
        nLow, mLow, nHigh, mHigh = nLow, mLow, min(nHigh, x - 1), min(mHigh, y - 1)
    else:
        nLow, mLow, nHigh, mHigh = x, y, x, y
ans = (nHigh - nLow + 1) * (mHigh - mLow + 1)
print(ans)