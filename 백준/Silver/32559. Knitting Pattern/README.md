# [Silver III] Knitting Pattern - 32559 

[문제 링크](https://www.acmicpc.net/problem/32559) 

### 성능 요약

메모리: 108080 KB, 시간: 88 ms

### 분류

수학

### 제출 일자

2024년 10월 30일 01:21:44

### 문제 설명

<p>Jörmunrekur had found himself with some extra time on his hands, so he decided to try to find a new hobby. After discussing this with some of his relatives, his grandparents lent him a book with knitting guides and knitting patterns.</p>

<p>He wants to start with something big, so he decides to make a sweater. He has also picked out a pattern from the book that he will repeat around the circumference of the sweater. He wants the pattern to be centered and then repeat out towards the back in either direction, but never wants to have less than the full pattern on the sweater. He will not place any patterns that leaves the placements of patterns asymmetric. Now he has to know how much empty space he should leave at the back of the sweater to achieve this.</p>

<p>The empty space that is not covered by the patterns must be a contiguous (possibly empty) section at the back of the sweater.</p>

### 입력 

 <p>The input contains two positive integers <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, the length of the sweater, and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D443 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$P$</span></mjx-container>, the length of the pattern. They satisfy <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D443 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>P</mi><mo>≤</mo><mi>N</mi><mo>≤</mo><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mn>18</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq P \leq N \leq 10^{18}$</span></mjx-container> and they have the same parity, as otherwise the pattern could never be perfectly centered.</p>

### 출력 

 <p>Print a single integer, the amount of empty space left on the back of the sweater.</p>

