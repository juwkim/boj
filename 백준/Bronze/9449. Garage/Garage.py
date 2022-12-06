W, H, w, h = map(int, input().split())
print(int((1 + H / h) // 2 * ((1 + W / w) // 2)))