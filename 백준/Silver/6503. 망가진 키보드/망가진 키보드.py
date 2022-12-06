while m := int(input()):
    txt = input()
    check = {}
    left, right, Max = 0, 0, 0
    while right < len(txt):
        if len(check) < m:
            if check.get(txt[right]):
                check[txt[right]] += 1
            else:
                check[txt[right]] = 1
            right += 1
        elif check.get(txt[right]):
            check[txt[right]] += 1
            right += 1
        else:
            if check[txt[left]] == 1:
                del check[txt[left]]
            else:
                check[txt[left]] -= 1
            Max = max(Max, right - left)
            left += 1
    print(max(Max, right - left))