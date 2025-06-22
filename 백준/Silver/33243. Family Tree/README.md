# [Silver I] Family Tree - 33243 

[문제 링크](https://www.acmicpc.net/problem/33243) 

### 성능 요약

메모리: 464280 KB, 시간: 888 ms

### 분류

자료 구조, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 해시를 사용한 집합과 맵, 문자열, 트리, 집합과 맵

### 제출 일자

2025년 6월 23일 01:38:05

### 문제 설명

<p>While you are attending the yearly family gathering of your family, you notice that your family keeps growing bigger and bigger. You are having a hard time remembering for every member of the family what their name is and to what part of the family they belong to. To solve this, you decide to create a family tree on a big sheet of paper. You collect a portrait picture from every member of the family and stick them onto the paper in the shape of a tree, putting pictures of children exactly one level below the picture of their parents.</p>

<p>Before actually sticking the pictures on the paper, you need to figure out how much paper you need. Environmentally aware as you are, you try to minimize the amount of paper needed. You decide to allow pictures within the same level to move to the left or right if this makes the tree less wide (see also the examples below).</p>

### 입력 

 <ul>
	<li>One line with one integer: <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><msup><mn>10</mn><mn>5</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \leq n \leq 10^5$</span></mjx-container>, the number of people in the family tree.</li>
	<li>One line that indicates the earliest ancestor that you have information about.</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n - 1$</span></mjx-container> lines, each in the format "<code>A - B</code>", indicating that <code>A</code> is the parent of <code>B</code>. These lines have no particular order.</li>
</ul>

<p>The name of each person consists of at most 20 characters from the English alphabet (<code>A-Z</code> and <code>a-z</code>).</p>

### 출력 

 <p>The minimum width of the family tree in the number of portrait pictures.</p>

