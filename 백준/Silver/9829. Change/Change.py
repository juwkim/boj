def solve():
    c5, c10, c20, c50, cost0 = map(int, input().split())
    if cost0 % 5 or 5 * c5 + 10 * c10 + 20 * c20 + 50 * c50 < cost0:
        return -1

    q50, r50 = divmod(cost0, 50)
    cnt50 = min(q50, c50)
    cost1 = cost0 - 50 * cnt50

    q20, r20 = divmod(cost1, 20)
    cnt20 = min(q20, c20)
    cost2 = cost1 - 20 * cnt20
    
    q10, r10 = divmod(cost2, 10)
    cnt10 = min(q10, c10)
    cost3 = cost2 - 10 * cnt10
    
    q5, r5 = divmod(cost3, 5)
    cnt5 = min(q5, c5)
    cost4 = cost3 - 5 * cnt5
    
    if cost4 == 0:
        cnt = cnt5 + cnt10 + cnt20 + cnt50
        return f"{cnt5} {cnt10} {cnt20} {cnt50} {cnt}"

    q50, r50 = divmod(cost0, 50)
    cnt50 = min(q50 - 1, c50)
    cost1 = cost0 - 50 * cnt50

    q20, r20 = divmod(cost1, 20)
    cnt20 = min(q20, c20)
    cost2 = cost1 - 20 * cnt20
    
    q10, r10 = divmod(cost2, 10)
    cnt10 = min(q10, c10)
    cost3 = cost2 - 10 * cnt10
    
    q5, r5 = divmod(cost3, 5)
    cnt5 = min(q5, c5)
    cost4 = cost3 - 5 * cnt5
    
    if cost4 == 0:
        cnt = cnt5 + cnt10 + cnt20 + cnt50
        return f"{cnt5} {cnt10} {cnt20} {cnt50} {cnt}"
    return -1

print(solve())