# [Bronze III] Provinces and Gold - 24803 

[문제 링크](https://www.acmicpc.net/problem/24803) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 많은 조건 분기(case_work), 구현(implementation), 수학(math)

### 문제 설명

<p>Jake is learning how to play the card game Dominion. In Dominion, you can buy a variety of treasure, action, and victory point cards - at the end of the game, the player with the most victory points wins!</p>

<p>Each turn, each player draws 5 cards and can use their action and treasure cards to obtain buying power in order to buy more cards. Since Jake is just starting out, he's decided to buy only treasure and victory point cards.</p>

<p>This means the cards he can buy are:</p>

<ul>
	<li>Province (costs $8$, worth $6$ victory points)</li>
	<li>Duchy (costs $5$, worth $3$ victory points)</li>
	<li>Estate (costs $2$, worth $1$ victory point)</li>
</ul>

<p>And, there are $3$ kinds of treasure cards:</p>

<ul>
	<li>Gold (costs $6$, worth $3$ buying power)</li>
	<li>Silver (costs $3$, worth $2$ buying power)</li>
	<li>Copper (costs $0$, worth $1$ buying power)</li>
</ul>

<p>At the start of Jake's turn, he draws $5$ of these cards. Given the number of Golds, Silvers, and Coppers in Jake's hand, calculate the best victory card and best treasure card he could buy that turn. Note that Jake can buy only one card.</p>

### 입력 

 <p>The input consists of a single test case on a single line, which contains three non-negative integers $G$, $S$, $C$ ($G + S + C \le 5$) indicating the number of Golds, Silvers, and Coppers Jake draws in his hand.</p>

### 출력 

 <p>Output the best victory card and the best treasure card Jake can buy this turn, separated with <code>" or "</code>, in this order. If Jake cannot afford any victory cards, output only the best treasure card he can buy.</p>

