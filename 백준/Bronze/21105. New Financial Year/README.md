# [Bronze III] New Financial Year - 21105 

[문제 링크](https://www.acmicpc.net/problem/21105) 

### 성능 요약

메모리: 28776 KB, 시간: 1028 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>Naomi has spent the past year tracking her doughnut sales. With so many different flavours, some are bound to sell more than others. In order to maximize her sales for the coming year, she keeps track of certain information on each flavor. She tracks exactly $N$ different flavours of doughnuts. For each flavour, she tracks $O$, the original price, $P$, the new price, and $C$, the relative change in price. The relative change in price is computed using the formula $C=100\% \cdot (P-O)/O$.</p>

<p>Unfortunately, during one of her late nights, while analyzing her clipboard of data, she spilled coffee over the entire section of the page that keeps track of the original price of each doughnut flavour.</p>

<p>Can you help Lesley recover her data, specifically $O$, the original price of each doughnut flavour?</p>

### 입력 

 <p>The first line contains a single integer $N$, the number of doughnut flavours ($1 \le N \le 10^4$).</p>

<p>Each of the following $N$ lines describes one flavour and contains two real numbers $P$ and $C$ ($1 \le P \le 1000.00$, $-1000.00 \le C \le 1000.00$), given to exactly 2 decimal places.</p>

### 출력 

 <p>Output $N$ lines. On line $i$, print $O$, the original price of the $i$-th doughnut flavour, with absolute or relative error at most $10^{-5}$.</p>

