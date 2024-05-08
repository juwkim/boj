# [Silver V] 평점 변환 - 31799 

[문제 링크](https://www.acmicpc.net/problem/31799) 

### 성능 요약

메모리: 145716 KB, 시간: 252 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2024년 5월 8일 20:29:12

### 문제 설명

<p>2023학년도까지 대구과고에서는 학생들의 한 학기 동안의 성적에 따라 A+, A0, A-, B+, B0, B-, C+, C0, C-의 아홉 가지 평어 가운데 하나를 부여하였다. 그러나 상대평가 중심의 평어 체제는 학생들 간의 과도한 경쟁을 유도하는 부작용이 있었다. 그래서 2024학년도부터는 B(Beginning), D(Developing), P(Proficient), E(Exceeding)의 네 가지 평어 가운데 하나를 부여하는 방식으로 체제를 바꿀 계획이다. 새로운 평어 체제는 상대평가 기간이 아닌 개인의 성장 과정에 따라 평어가 부여되는 방식이므로 기존 평어 체제의 문제점을 해결할 것으로 기대하고 있다.</p>

<p>대구과고 학생들은 2023학년도 이전과 2024학년도 이후의 평어 체제가 완전히 달라서 자신의 발전 과정을 정확하게 알기 어려워졌다. 이에 따라 2023학년도 이전의 평어를 새로운 평어 체제에 맞추어 변환하는 공식적인 기준을 발표하였다.</p>

<ul>
	<li>평어가 C+, C0, C- 가운데 하나이면, 새로운 평어는 B이다.</li>
	<li>평어가 B0, B- 가운데 하나이면
	<ul>
		<li>첫 학기이거나 이전 학기의 평어가 C+, C0, C- 가운데 하나이면, 새로운 평어는 D이다.</li>
		<li>이전 학기의 평어가 A+, A0, A-, B+, B0, B- 가운데 하나이면, 새로운 평어는 B이다.</li>
	</ul>
	</li>
	<li>평어가 A-, B+ 가운데 하나이면
	<ul>
		<li>첫 학기이거나 이전 학기의 평어가 B0, B-, C+, C0, C- 가운데 하나이면, 새로운 평어는 P이다.</li>
		<li>이전 학기의 평어가 A+, A0, A-, B+ 가운데 하나이면, 새로운 평어는 D이다.</li>
	</ul>
	</li>
	<li>평어가 A0이면
	<ul>
		<li>첫 학기이거나 이전 학기의 평어가 A-, B+, B0, B-, C+, C0, C- 가운데 하나이면, 새로운 평어는 E이다.</li>
		<li>이전 학기의 평어가 A+, A0 가운데 하나이면, 새로운 평어는 P이다.</li>
	</ul>
	</li>
	<li>평어가 A+이면 새로운 평어는 E이다.</li>
</ul>

<p>대구과고에 다니는 은성이는 기존 평어 체제로 부여되었던 자신의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>학기 동안의 평어를 새로운 평어 체제에 맞게 변환하고 싶다. 하지만 평어 변환 기준이 너무 복잡해 여러분에게 대신 이 일을 맡기려고 한다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>학기 동안의 평어가 첫 학기부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>번째 학기까지 순서대로 공백 없이 주어질 때, 새로운 평어 체제에 맞게 변환한 결과를 출력하는 프로그램을 작성하라. <strong>단, 은성이는 A0, B0, C0에서 실수로 0을 생략하여 'A', 'B', 'C'와 같이 적을 때도 있다고 한다.</strong></p>

### 입력 

 <p>첫 번째 줄에 은성이가 대구과고에 다닌 학기의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>두 번째 줄에 은성이의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>학기 동안의 평어를 공백 없이 순서대로 나열한 문자열이 주어진다.</p>

### 출력 

 <p>은성이의 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>학기 동안의 평어를 새로운 체제에 맞게 변환한 결과를 첫 학기부터 공백 없이 순서대로 나열한 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>의 문자열을 출력한다.</p>

