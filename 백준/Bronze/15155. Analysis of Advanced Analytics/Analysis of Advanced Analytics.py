N, K = map(int, input().split())
pages = [*map(int, input().split())]
note, r = 1, K
for page in pages:
    if r < page:
        r = K - page
        note += 1
    else:
        r -= page
print(note)