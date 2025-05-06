# [Silver V] High Towers - 33785 

[문제 링크](https://www.acmicpc.net/problem/33785) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

조합론, 수학

### 제출 일자

2025년 5월 6일 18:47:19

### 문제 설명

<p>Peter really likes to solve puzzles and his friends know this. They recently asked Peter to solve a well-known puzzle: given a triangular figure of height <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container> (see the figure right), how many triangles pointing upwards are in the figure? Peter solved this problem in no-time so he asked his friends for some harder puzzles. And they came up with the same figure of height <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container> and height <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container> which Peter easily solved.</p>

<p>However, Peter got himself in a bit of trouble when his friends want him to solve the puzzle with a figure of height <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$6$</span></mjx-container>. Peter still wants to impress his friends with the correct answer, and he wants to be able to solve the puzzles with an even greater height, possibly up to two million! Since he's a very bad programmer, he asked you for help: given the height of the triangle <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>, can you determine how many triangles pointing upwards there are visible in the figure?</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/673fc3a8-5341-4650-9955-5c5814eff4c3/-/preview/" style="width: 250px; height: 250px;"></p>

<p style="text-align: center;">Figure 1 - A triangle puzzle with height 3. There are 10 upward triangles in this figure.</p>

### 입력 

 <p>The input consists of one integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c22C5"></mjx-c></mjx-mo><mjx-msup space="3"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>2</mn><mo>⋅</mo><msup><mn>10</mn><mn>6</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$ 1 \leq n \leq 2 \cdot 10^6 $</span></mjx-container>): the height of the triangle.</p>

### 출력 

 <p>One integer with the number of triangles pointing upwards in the figure.</p>

