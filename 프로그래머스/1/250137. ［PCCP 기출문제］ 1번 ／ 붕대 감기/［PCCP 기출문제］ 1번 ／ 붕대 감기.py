def solution(bandage, health, attacks):
    t, x, y = bandage
    cur = health
    prev_attack_time = 0
    for attack_time, damage in attacks:
        heal_time = attack_time - prev_attack_time - 1
        cur = min(health, cur + heal_time * x + (heal_time // t) * y)
        cur -= damage
        prev_attack_time = attack_time
        if cur <= 0:
            return -1
    return cur