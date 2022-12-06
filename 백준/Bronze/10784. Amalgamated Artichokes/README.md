# [Bronze I] Amalgamated Artichokes - 10784 

[문제 링크](https://www.acmicpc.net/problem/10784) 

### 성능 요약

메모리: 114328 KB, 시간: 204 ms

### 분류

Empty

### 문제 설명

<p>Fatima Cynara is an analyst at Amalgamated Artichokes (AA). As with any company, AA has had some very good times as well as some bad ones. Fatima does trending analysis of the stock prices for AA, and she wants to determine the largest decline in stock prices over various time spans. For example, if over a span of time the stock prices were 19, 12, 13, 11, 20 and 14, then the largest decline would be 8 between the first and fourth price. If the last price had been 10 instead of 14, then the largest decline would have been 10 between the last two prices.</p>

<p>Fatima has done some previous analyses and has found that the stock price over any period of time can be modelled reasonably accurately with the following equation:</p>

<p style="text-align:center">price(k) = p·(sin(a·k+b) + cos(c·k+d) + 2)</p>

<p>where p, a, b, c and d are constants. Fatima would like you to write a program to determine the largest price decline over a given sequence of prices. Figure A.1 illustrates the price function for Sample Input 1.</p>

<p>You have to consider the prices only for integer values of k.</p>

<p style="text-align:center"><img alt="" src="" style="height:270px; width:561px"></p>

<p style="text-align:center">Figure A.1: Sample Input 1. The largest decline occurs from the fourth to the seventh price.</p>

### 입력 

 <p>The input consists of a single line containing 6 integers p (1 ≤ p ≤ 1 000), a, b, c, d (0 ≤ a, b, c, d ≤ 1 000) and n (1 ≤ n ≤ 10<sup>6</sup>). The first 5 integers are described above. The sequence of stock prices to consider is price(1), price(2), ... , price(n).</p>

### 출력 

 <p>Display the maximum decline in the stock prices. If there is no decline, display the number 0. Your output should have an absolute or relative error of at most 10<sup>−6</sup>.</p>

