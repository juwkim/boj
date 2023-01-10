from random import shuffle

for t in range(1, 1 + int(input())):

    input()
    txt_list = input().split()
    ans = 'IMPOSSIBLE'
    if all(len(txt) != 1 for txt in txt_list):
        buf = [*map(chr, range(65, 91))]
        ans = ''.join(buf)
        cnt = 1
        while any(txt in ans for txt in txt_list):
            shuffle(buf)
            ans = ''.join(buf)
            cnt += 1
            if cnt == 2000:
                break
        if cnt == 2000:
            ans = 'IMPOSSIBLE'
    print(f'Case #{t}: {ans}')