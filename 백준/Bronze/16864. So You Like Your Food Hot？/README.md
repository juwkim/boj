# [Bronze II] So You Like Your Food Hot? - 16864 

[문제 링크](https://www.acmicpc.net/problem/16864) 

### 성능 요약

메모리: 2016 KB, 시간: 8 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>Peter is co-owner of the incredibly successful Pete and Pat’s Pitas and Pizzas and his sales are on fire! But unfortunately, so is his building, due to carelessly laid delivery boxes placed too close to Pete’s famous wood burning pizza oven. After sifting though the remnants, one of the few things Pete is able to salvage is a ledger book, but the only thing he can make out on the charred pages is the profit he made during the last month. The insurance company would like to know how many pitas and how many pizzas Pete actually delivered over that period. Pete does recall how much profit he makes on each of these products, so he’s pretty confident that he can determine how many of each were sold during the last month given the total profit. Well perhaps “confident” is not the exact word Peter is looking for – it’s more like clueless. Can you help Pete out? I’m sure there are some discount coupons in it for you, or at least a really cheap price on a used pizza oven.</p>

### 입력 

 <p>Input consists of a single line containing 3 values p<sub>t</sub> p<sub>1</sub> p<sub>2</sub>, where 0 ≤ p<sub>t</sub> ≤ 10 000.00 is the profit for the month and 0 < p<sub>1</sub>, p<sub>2</sub> ≤ 100.00 are the profits Pete makes on a pita (p<sub>1</sub>) and on a pizza (p<sub>2</sub>). All values are in dollars and cents.</p>

### 출력 

 <p>Display two integers: the number of pitas sold and the number of pizzas sold so that the total profit equals the value given. If there is more than one combination of pitas and pizzas that give the specified profit, list them all, one combination per line, listing the combination with the smallest number of pitas first, then the combination with the second smallest number of pitas, and so on. If there are no combinations of pizza and pita sales that realize the profit, output <code>none</code>.</p>

