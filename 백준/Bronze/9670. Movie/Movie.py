g = lambda: [*map(int, input().split())]

price = (319, 419, 450, 519, 599, 600, 630, 719)
resolution = ((768, 1024), (600, 1024), (640, 960), (1536, 2048), (640, 1136), (800, 1280), (1080, 1920), (640, 1136))

def check(W, H, a, b):
    
    s = int(a * H / W) / b
    t = int(b * W / H) / a

    if a * H == b * W:
        return max(s, t)
    else:
        return min(s, t)

while sum(s:= g()):
    W, H = sorted(s)
    nums = [max(check(H, W, a, b), check(W, H, a, b)) for a, b in resolution]
    MIN = max(nums)
    idx = min([i for i in range(len(resolution)) if nums[i] == MIN])

    print(price[idx])