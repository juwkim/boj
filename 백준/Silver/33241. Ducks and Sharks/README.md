# [Silver IV] Ducks and Sharks - 33241 

[문제 링크](https://www.acmicpc.net/problem/33241) 

### 성능 요약

메모리: 112012 KB, 시간: 180 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 정렬, 문자열

### 제출 일자

2025년 2월 23일 15:19:59

### 문제 설명

<p>The Ducks and the Sharks have had many adventures in the past year. Because the weather has been so nice lately, they want to organise a water polo tournament. After forming the teams, every team plays one match against every other team. Being caught up in the fun of playing the matches, they don't feel like figuring out who won, so they turn to you for help.</p>

<p>You receive a list of matches and the number of goals made by both teams in a match. For each match, the winner gets 3 points, the loser gets 0 points, and in case of a draw both teams get 1 point. It is your job to figure out which teams got the most points, and provide a top five of the best teams.</p>

### 입력 

 <ul>
	<li>One line with one integer: <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c34"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>400</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \leq n \leq 400$</span></mjx-container>, the number of teams.</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mfrac><mjx-frac><mjx-num><mjx-nstrut></mjx-nstrut><mjx-mrow size="s"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c22C5"></mjx-c></mjx-mo><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-mrow></mjx-num><mjx-dbox><mjx-dtable><mjx-line></mjx-line><mjx-row><mjx-den><mjx-dstrut></mjx-dstrut><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mrow><mi>n</mi><mo>⋅</mo><mo stretchy="false">(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mn>2</mn></mfrac></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\frac{n \cdot (n - 1)}2$</span></mjx-container> lines (one for each match), containing the names of the two teams and the number of goals both teams made during that match (all separated by one space).
	<ul>
		<li>The name of each team consists of at most 20 characters from the English alphabet (<code>A-Z</code> and <code>a-z</code>).</li>
		<li>The scores are between <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container> (inclusive).</li>
	</ul>
	</li>
</ul>

<p>Note that every team plays exactly once against every other team.</p>

### 출력 

 <p>The names of the <em>top five teams</em> in the water polo competition, followed by their total obtained score. Each team name should be written on a separate line. Each team name and score should be separated by exactly one space. Note:</p>

<ul>
	<li>If there are less than five teams participating, simply list all participants (see example 1).</li>
	<li>If there are two teams with the same score, order them alphabetically (see example 2).</li>
</ul>

