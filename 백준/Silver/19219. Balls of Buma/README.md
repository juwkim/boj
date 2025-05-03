# [Silver I] Balls of Buma - 19219 

[문제 링크](https://www.acmicpc.net/problem/19219) 

### 성능 요약

메모리: 111580 KB, 시간: 104 ms

### 분류

애드 혹, 그리디 알고리즘

### 제출 일자

2025년 5월 4일 04:09:41

### 문제 설명

<p>Balph is learning to play a game called Buma. In this game, he is given a row of colored balls. He has to choose the color of one new ball and the place to insert it (between two balls, or to the left of all the balls, or to the right of all the balls).</p>

<p>When the ball is inserted the following happens repeatedly: if some segment of balls of the same color became longer as a result of a previous action and its length became at least <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>, then all the balls of this segment are eliminated. </p>

<p>Consider, for example, a row of balls '<code>AAABBBWWBB</code>'. Suppose Balph chooses a ball of color '<code>W</code>' and the place to insert it after the sixth ball, i. e. to the left of the two '<code>W</code>'s. After Balph inserts this ball, the balls of color '<code>W</code>' are eliminated, since this segment was made longer and has length <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container> now, so the row becomes '<code>AAABBBBB</code>'. The balls of color '<code>B</code>' are eliminated now, because the segment of balls of color '<code>B</code>' became longer and has length <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container> now. Thus, the row becomes '<code>AAA</code>'. However, none of the balls are eliminated now, because there is no elongated segment.</p>

<p>Help Balph count the number of possible ways to choose a color of a new ball and a place to insert it that leads to the elimination of all the balls.</p>

### 입력 

 <p>The only line contains a non-empty string of uppercase English letters of length at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c22C5"></mjx-c></mjx-mo><mjx-msup space="3"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>⋅</mo><msup><mn>10</mn><mn>5</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3 \cdot 10^5$</span></mjx-container>. Each letter represents a ball with the corresponding color.</p>

### 출력 

 <p>Output the number of ways to choose a color and a position of a new ball in order to eliminate all the balls.</p>

