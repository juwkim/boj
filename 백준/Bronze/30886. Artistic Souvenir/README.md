# [Bronze III] Artistic Souvenir - 30886 

[문제 링크](https://www.acmicpc.net/problem/30886) 

### 성능 요약

메모리: 108080 KB, 시간: 132 ms

### 분류

사칙연산, 기하학, 수학

### 제출 일자

2023년 12월 1일 03:23:31

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/c3a2639a-5d4b-4134-8aeb-82f13cacd422/-/preview/" style="width: 300px; height: 300px;"></p>

<p style="text-align: center;">A typical circular design on a square Delft tile.</p>

<p>Delft is world-famous for its blue and white pottery (also known as <em>Delfts blauw</em>), and the earliest pieces date back to the 16th century.</p>

<p>During a stroll in Delft, Christiaan sees a lot of beautifully painted pottery objects like plates, tiles, and vases in the souvenir shops. Inspired by those, he decides to hand paint such a square tile himself. He has already picked a circular design he wants to place in the middle of the tile. He would like to leave a margin of at least <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-c63"></mjx-c><mjx-c class="mjx-c6D"></mjx-c></mjx-mtext></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mtext>cm</mtext></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \text{cm}$</span></mjx-container> around the design. Now, Christiaan just needs to buy a square tile of a suitable size.</p>

<p>Given the area of the circular design, what is the minimum area of the square tile?</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>a</mi><mo>≤</mo><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mn>15</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq a\leq 10^{15}$</span></mjx-container>), the area of the circular design in <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mtext class="mjx-n"><mjx-c class="mjx-c63"></mjx-c><mjx-c class="mjx-c6D"></mjx-c></mjx-mtext><mjx-script style="vertical-align: 0.363em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mtext>cm</mtext><mn>2</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\text{cm}^2$</span></mjx-container>.</li>
</ul>

### 출력 

 <p>Output the minimum area of the square tile in <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mtext class="mjx-n"><mjx-c class="mjx-c63"></mjx-c><mjx-c class="mjx-c6D"></mjx-c></mjx-mtext><mjx-script style="vertical-align: 0.363em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mtext>cm</mtext><mn>2</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\text{cm}^2$</span></mjx-container> that is needed for a design with area <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$a$</span></mjx-container> if Christiaan wants to leave a margin of at least <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-c63"></mjx-c><mjx-c class="mjx-c6D"></mjx-c></mjx-mtext></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mtext>cm</mtext></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \text{cm}$</span></mjx-container> around the design.</p>

<p>Your answer should have an absolute or relative error of at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mo>−</mo><mn>9</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^{-9}$</span></mjx-container>.</p>

