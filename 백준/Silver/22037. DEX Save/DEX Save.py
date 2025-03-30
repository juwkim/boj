from itertools import product

def d20_outcomes(roll_type):
    """주어진 roll_type (straight, advantage, disadvantage)에 따른 d20 결과 확률 분포"""
    outcomes = [i for i in range(1, 21)]
    
    if roll_type == "straight":
        return {i: 1/20 for i in outcomes}
    
    if roll_type == "advantage":
        # 두 개의 d20을 굴려 최댓값 선택
        advantage_probs = {i: 0 for i in outcomes}
        for a, b in product(outcomes, repeat=2):
            advantage_probs[max(a, b)] += 1
        total = 20 * 20
        return {k: v / total for k, v in advantage_probs.items()}
    
    if roll_type == "disadvantage":
        # 두 개의 d20을 굴려 최솟값 선택
        disadvantage_probs = {i: 0 for i in outcomes}
        for a, b in product(outcomes, repeat=2):
            disadvantage_probs[min(a, b)] += 1
        total = 20 * 20
        return {k: v / total for k, v in disadvantage_probs.items()}

def bonus_dice_outcomes(bonus_dice):
    """보너스 주사위(예: +d6, -d4 등)의 확률 분포 생성"""
    if not bonus_dice:
        return {0: 1.0}  # 아무 변화 없음
    
    bonus_distributions = []
    
    for sign, sides in bonus_dice:
        dice_outcomes = [sign * i for i in range(1, sides + 1)]
        probability = 1 / sides
        bonus_distributions.append({x: probability for x in dice_outcomes})
    
    # 여러 개의 주사위 조합 확률을 계산 (convolution 방식)
    final_outcomes = {0: 1.0}  # 초기값
    
    for dice_distribution in bonus_distributions:
        new_outcomes = {}
        for (prev_sum, prev_prob) in final_outcomes.items():
            for (dice_value, dice_prob) in dice_distribution.items():
                new_outcomes[prev_sum + dice_value] = new_outcomes.get(prev_sum + dice_value, 0) + prev_prob * dice_prob
        final_outcomes = new_outcomes
    
    return final_outcomes

def compute_success_probability(d, m, roll_type, bonus_dice):
    """주어진 조건에서 성공 확률 계산"""
    d20_probs = d20_outcomes(roll_type)
    bonus_probs = bonus_dice_outcomes(bonus_dice)
    
    success_prob = 0.0
    
    for d20_result, d20_prob in d20_probs.items():
        if d20_result == 1:  # 자동 실패
            continue
        if d20_result == 20:  # 자동 성공
            success_prob += d20_prob
            continue
        
        for bonus_value, bonus_prob in bonus_probs.items():
            total_roll = d20_result + m + bonus_value
            if total_roll >= d:
                success_prob += d20_prob * bonus_prob
    
    return success_prob

# 입력 처리
d, m = map(int, input().split())
roll_type = input().strip()
bonus_info = input().split()

k = int(bonus_info[0])
bonus_dice = []
for i in range(1, k + 1):
    sign = 1 if bonus_info[i][0] == '+' else -1
    sides = int(bonus_info[i][2:])
    bonus_dice.append((sign, sides))

# 확률 계산 및 출력
result = compute_success_probability(d, m, roll_type, bonus_dice)
print(f"{result:.6f}")
