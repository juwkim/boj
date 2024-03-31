# [Bronze IV] 특별한 가지 - 31668 

[문제 링크](https://www.acmicpc.net/problem/31668) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 3월 31일 22:29:43

### 문제 설명

<blockquote>
<p>이거나 가지세요...</p>
</blockquote>

<p>작년 NLCS Jeju는 "파마산을 묻혀 튀긴 소고기", 이하 "파묻튀"에 반대하는 학생들의 가지 운동을 막아내고 신메뉴 "파마산을 묻혀 튀긴 소고기를 넣은 김밥", 이하 "파묻튀밥"을 출시하였다.</p>

<p>그러나 학생들은 파묻튀보다는 신선한 가지를 먹고 싶어 한다! 따라서 학생들은 가지를 구매하여 오늘 급식에 나올 파묻튀밥에 들어있는 파묻튀를 모두 가지로 바꿔치기로 하였다. 이를 위해 학생들은 구매해야 하는 가지의 양을 알아내야 한다. </p>

<ul>
	<li>파묻튀밥 한 줄에는 파묻튀가 정확히 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>그램 들어간다.</li>
	<li>학교는 오늘 파묻튀밥을 만들기 위해 파묻튀를 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>그램 사용하였다.</li>
	<li>학교가 만드는 파묻튀밥의 줄 수는 정수이다. 예를 들어, 학교가 파묻튀밥을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c2E"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2.5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2.5$</span></mjx-container>줄 만드는 일은 일어날 수 없다.</li>
	<li>파묻튀밥 한 줄의 파묻튀는 정확히 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>그램의 가지로 바꿔치기해야 한다.</li>
</ul>

<p>학교에서 제작한 파묻튀밥의 파묻튀를 모두 가지로 바꿔치기하기 위해 학생들이 구매해야 하는 가지의 양의 최솟값을 구해주자.</p>

### 입력 

 <p>첫 번째 줄에 파묻튀밥 한 줄에 들어가는 파묻튀의 양을 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>두 번째 줄에 학교가 파묻튀를 사용한 양을 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 주어진다.</p>

<p>세 번째 줄에 파묻튀밥 한 줄에 필요한 가지의 양을 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>가 주어진다.</p>

### 출력 

 <p>한 줄에 학생들이 구매해야 하는 가지의 양의 최솟값을 그램 단위로 출력한다.</p>

