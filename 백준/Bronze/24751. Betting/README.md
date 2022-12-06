# [Bronze IV] Betting - 24751 

[문제 링크](https://www.acmicpc.net/problem/24751) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>The popular streaming platform switch.tv just unveiled their newest feature: switch betting.  Streamers can now get their viewers to bet on two different options using switch points (patented).</p>

<p>Each viewer bets some number of switch points for one of the two options. The total amount of switch points bet by everyone is called the prize pool. The streamer will choose one of the options as the winner and the prize pool is split (not necessarily equally) between all the viewers who bet on that option; the more you bet on the option, the more of the prize pool you receive. In particular, if you contributed $p\%$ of all the bets for one of the options and that option wins, then you receive $p\%$ of the total prize pool.</p>

<p>The switch.tv team has come to you to compute what the switch point payout is for each viewer if their selected option wins. To do this, they ask you to find the switch-payout-ratio for each of the two options. Since the payout to each viewer is proportional to the number of switch points they put into the bet, the switch team will be able to use this ratio to determine each viewer's winnings.</p>

<p>For example, suppose a streamer created a switch bet where three viewers participated. Two viewers bet $10$ and $30$ switch points on option one and the last viewer bets $10$ switch points on option two. We can see that option one has $80\%$ of the bets and option two has $20\%$ of the bets.</p>

<p>If option one wins, then the two viewers who bet on that receive $12.5$ and $37.5$ switch points, respectively, which means that the switch-payout-ratio is $1$:$1.25$ for option one. If option two wins, then the single viewer who bets on that receives 50 switch points, which means that the switch-payout-ratio is $1$:$5$.</p>

<p>Given the percentage of total bets for option one, help switch.tv by computing the switch-payout-ratio for the two options.</p>

### 입력 

 <p>The input consists of one integer $a$ ($0 < a < 100$), which is the percentage of switch points bet on option one.</p>

### 출력 

 <p>For each option (option one, then option two), display the number <code>x</code> such that <code>1:x</code> is the switch-payout-ratio for that option. Your answer should have an absolute or relative error of at most $10^{-3}$.</p>

