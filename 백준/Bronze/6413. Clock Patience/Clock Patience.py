while (s:= input()) != '#':
    cards = s.split()
    for _ in range(3):
        cards.extend(input().split())
    
    stack = [[] for _ in range(13)]
    for i in range(51, -1, -1):
        stack[12 - i % 13].append(cards[i])
    
    cnt = 0
    cur = 12
    table = {'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    while stack[cur]:
        card = stack[cur].pop()
        cur = table.get(card[0], ord(card[0]) - ord('0')) - 1
        cnt += 1
    print(f'{cnt:02d},{card}')