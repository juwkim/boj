def main():
    while True:
        pl = int(input())
        if pl == 0:
            exit()
        cn = int(input())
        w = int(input())
        cs = int(input())
        lines = []
        line = input()
        while line != '?':
            lines.append(line)
            line = input()
            if len(line) == 0:
                line = '.' * w

        page = [[['.'] * w for _ in range(pl)] for _ in range(cn)]
        i = j = 0
        eol = False
        while i < len(lines):
            for a in range(cn):
                if eol:
                    break
                for b in range(pl):
                    if eol:
                        break
                    for c in range(w):
                        page[a][b][c] = lines[i][j]
                        j += 1
                        if j >= len(lines[i]):
                            i += 1
                            if i >= len(lines):
                                eol = True
                            else:
                                j = 0
                            break

            for a in range(pl):
                out = ''
                for b in range(cn):
                    out += ''.join(page[b][a])
                    if b < cn - 1:
                        out += '.' * cs
                print(out)
            print('#')

            page = [[['.'] * w for _ in range(pl)] for _ in range(cn)]

        print('?')


if __name__ == '__main__':
    main()

