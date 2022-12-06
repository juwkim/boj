while n:=int(input()):
    check = [0] * n
    pages = input().split(',')
    for page in pages:
        if '-' in page:
            a, b = map(int, page.split('-'))
            for i in range(a-1, min(b, n)):
                check[i] = 1
        elif int(page) <= n:
            check[int(page)-1] = 1
    print(sum(check))