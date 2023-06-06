from math import dist
x1, y1, x2, y2 = map(float, input().split())

ans = "The gopher cannot escape."
while True:
    try:
        x3, y3 = map(float, input().split())
        if dist((x2, y2), (x3, y3)) > dist((x1, y1), (x3, y3)) * 2:
            ans = f"The gopher can escape through the hole at ({x3:.3f},{y3:.3f})."
            break
    except:
        break
print(ans)