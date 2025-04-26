for tc in range(1, int(input()) + 1):
    input()
    a, b = 0, 0
    for v in map(int, input().split()): a, b = b, max(b, a + v)
    print(f"Data Set {tc}:\n{b}\n")