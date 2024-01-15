# [Silver III] 엠비티아이 - 24725 

[문제 링크](https://www.acmicpc.net/problem/24725) 

### 성능 요약

메모리: 112532 KB, 시간: 256 ms

### 분류

브루트포스 알고리즘, 구현, 문자열

### 제출 일자

2024년 1월 15일 16:45:30

### 문제 설명

<p>Myers-Briggs Type Indicator (MBTI) is an introspective self-report questionnaire indicating differing psychological preferences in how people perceive the world and make decisions. </p>

<p>MBTI divides human personality into 16 types and each type consists of 4 alphabets.</p>

<ul>
	<li>The first letter represents extroversion (<strong>E</strong>) or introversion (<strong>I</strong>), indicating how they gain their energy.</li>
	<li>The second letter represents intuition (<strong>N</strong>) or sensation (<strong>S</strong>), indicating how new information is understood and interpreted.</li>
	<li>The third letter represents emotions (<strong>F</strong>) or thinking (<strong>T</strong>), indicating how they make decisions.</li>
	<li>The last letter represents perception (<strong>P</strong>) or judgment (<strong>J</strong>), indicating lifestyle preferences how they organize their time.</li>
</ul>

<p>There are 16 types of MBTI because a total of four alphabets are selected according to each description (e.g. <strong>ENFP</strong>, <strong>ISTP</strong>, <strong>ENTJ</strong>, etc.) </p>

<p>One day, you find an alphabet board while going to the laboratory. As you are too obsessed with MBTI, you start looking for how many MBTI types are on the board. If the four horizontal, vertical, or diagonal letters on the board are one of the types of MBTI, you will shout "<strong>MBTI!</strong>". The direction of the word does not matter, i.e. it could be the bottom right to top left, left to right, and so on. Also, even though the type is previously found, "<strong>MBTI!</strong>" should be shouted again if the word is in a different location or direction.</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/21efb880-a4c9-428e-a069-513e79468fe5/-/preview/" style="width: 168px; height: 150px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/11bd8db4-cee4-4be2-8e9a-60cd8ccc966a/-/crop/873x780/3,0/-/preview/" style="height: 150px; width: 168px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/787300a6-36c6-488a-a13d-50d731e96196/-/crop/878x781/0,0/-/preview/" style="width: 169px; height: 150px;"></td>
		</tr>
		<tr>
			<td><strong>Figure 1.</strong></td>
			<td><strong>Figure 2.</strong></td>
			<td><strong>Figure 3.</strong></td>
		</tr>
	</tbody>
</table>

<p> Let's find all the MBTI types on the board and shout "<strong>MBTI!</strong>" together.</p>

### 입력 

 <p>Your program is to read from standard input. The input starts with an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>,</mo><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N, M$</span></mjx-container> ( <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>,</mo><mi>M</mi><mo>≤</mo><mn>200</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N,M \leq 200$</span></mjx-container> ) representing rows and columns of boards. Following this are <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> lines containing <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container> uppercase characters how does the alphabet board consist with.</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line. The line should contain total occurrences of 16 MBTI types, which will be equal to the number of times you shouted '<strong>MBTI!</strong>'</p>

