def is_silly(a, b):
    quiet = None
    k = i + 1
    for j in range(i + 1, len(pressed)):
        if k < len(typed) and (pressed[j] == typed[k] or (pressed[j] == a and typed[k] == b)):
            k += 1
            continue
        if pressed[j] == a:
            return False, ''
        if quiet is None:
            quiet = pressed[j]
        elif quiet != pressed[j]:
            return False, ''
    return True, quiet

pressed = input()
typed = input()
i = 0
while pressed[i] == typed[i]:
    i += 1
a, b = pressed[i], typed[i]
if len(pressed) == len(typed):
    print(a, b)
    print('-')
else:
    res, quiet = is_silly(a, b)
    if not res:
        quiet = a
        k = i
        for j in range(i + 1, len(pressed)):
            if pressed[j] == quiet:
                continue
            if pressed[j] == typed[k]:
                k += 1
                continue
            a, b = pressed[j], typed[k]
            break
    print(a, b)
    print(quiet)