import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

item = {}
hand = Counter()
profit = 0
while (s:=input()) != '*':
    match s[0]:
        case 'n':
            _, name, buy, sell = s.split()
            item[name] = float(buy), float(sell)
        case 'b':
            _, name, count = s.split()
            hand[name] += int(count)
        case 's':
            _, name, count = s.split()
            count = int(count)
            hand[name] -= count
            profit += count * (item[name][1] - item[name][0])
        case 'd':
            _, name = s.split()
            profit -= hand[name] * item[name][0]
            del item[name], hand[name]
        case 'r':
            print("                  INVENTORY REPORT")
            print("Item Name     Buy At      Sell At      On Hand        Value")
            print("---------     ------      -------      -------        -----")
            for name, (buy, sell) in sorted(item.items()):
                print(f"{name:9}     {buy:6.2f}      {sell:7.2f}      {hand[name]:7}      {hand[name] * buy:7.2f}")
            print("------------------------")
            print(f"Total value of inventory {sum(hand[name] * buy for name, (buy, _) in item.items()):34.2f}")
            print(f"Profit since last report {profit:34.2f}")
            print()
            profit = 0