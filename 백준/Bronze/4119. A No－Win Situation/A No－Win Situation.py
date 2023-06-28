def score(card, score, has_ace):
    if card == 'A':
        if has_ace:
            score += 1
        else:
            has_ace = True
            score += 11
    elif card in "KQJT":
        score += 10
    else:
        score += int(card)
    if score > 21 and has_ace:
        score -= 10
        has_ace = False
    return score, has_ace

while (deck:= input()) != "JOKER":
    
    ans = "No"
    player, p_has_ace = score(deck[0], 0, False)
    player, p_has_ace = score(deck[2], player, p_has_ace)
    dealer_base, d_has_ace_base = score(deck[1], 0, False)
    dealer_base, d_has_ace_base = score(deck[3], dealer_base, d_has_ace_base)
    
    if len(deck) == 4:
        if player >= dealer_base:
            ans = "Yes"
    else:
        for i in range(4, len(deck)):
    
            dealer, d_has_ace = dealer_base, d_has_ace_base
            j = i
            while j < len(deck) and dealer < 17:
                dealer, d_has_ace = score(deck[j], dealer, d_has_ace)
                j += 1
            if dealer > 21 or player >= dealer:
                ans = "Yes"
                break
            player, p_has_ace = score(deck[i], player, p_has_ace)
            if player > 21:
                break
    print(ans)