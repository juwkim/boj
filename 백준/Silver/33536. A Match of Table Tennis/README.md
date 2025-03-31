# [Silver III] A Match of Table Tennis - 33536 

[문제 링크](https://www.acmicpc.net/problem/33536) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

사칙연산, 많은 조건 분기, 구현, 수학, 파싱, 문자열

### 제출 일자

2025년 3월 31일 10:05:58

### 문제 설명

<p>The rules of a match of table tennis are quite easy. When a match is played best of five games, it means that the player who wins three games wins. Since there is no point of playing after a winner is decided only the following results are possible: 3-0, 3-1, 3-2, 0-3, 1-3 and 2-3. For each game, the first player to reach 11 points wins that game. However, a game must be won by at least a two point margin. Therefore scores such as 9-12 and 17-14 are not possible, but 9-11, 12-10 and 4-8 are. Each player serves two points in a row and then switch server. However, if a score of 10-10 is reached in any game, then each server serves only one point before the server is switched. In the first game the guest player starts serving, the next game the host starts serving, ect. Both players can score a point, not just the server.</p>

<p>While playing a match of table tennis players are often confused and don't know who the server is. You should help the table tennis players with a program, which can decide who the server is based on the scores. Since people can make mistakes while giving input to the program, you should also check for consistency. Note that you can only start a new game, when the previous game has a winner. </p>

### 입력 

 <p>On the first line a single integer n, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq n \leq 5$</span></mjx-container>, the number of games played. On the second line <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> scores in the form <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>−</mo><mi>b</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a-b$</span></mjx-container>, with <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>≤</mo><mn>99</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \leq a, b \leq 99$</span></mjx-container>. </p>

### 출력 

 <p>Output "HOST" when the host player is serving, "GUEST" when the guest player is serving or "INCONSISTENT" when the input is not correct. </p>

