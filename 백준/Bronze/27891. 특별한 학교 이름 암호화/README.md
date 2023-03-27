# [Bronze II] 특별한 학교 이름 암호화 - 27891 

[문제 링크](https://www.acmicpc.net/problem/27891) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현, 문자열

### 문제 설명

<p>GEC에는 여러 학교가 있다. 각 학교의 약칭과 정식 명칭은 다음과 같다.</p>

<ul>
	<li>NLCS: North London Collegiate School</li>
	<li>BHA: Branksome Hall Asia</li>
	<li>KIS: Korea International School</li>
	<li>SJA: St. Johnsbury Academy</li>
</ul>

<p>학교 이름을 싫어하는 동호는, 학교들의 이름을 암호화해 버렸다!</p>

<p>동호가 이름을 암호화하는 방법은 다음과 같다. 이 문제에서 암호화되는 이름은 정식 명칭임에 유의한다.</p>

<ul>
	<li>이름에 있는 모든 공백과 문장 부호를 제거한다.</li>
	<li>이름의 모든 대문자를 소문자로 바꾼다.</li>
	<li>이름의 첫 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10$</span></mjx-container>글자를 제외한 모든 글자를 지운다.</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>에서 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>25</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$25$</span></mjx-container>까지의 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>을 하나 고른 후, 이름의 모든 글자를 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>칸 앞으로 이동시킨다.</li>
</ul>

<p>문자를 앞으로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>칸 이동시킨다는 것은 a를 b로, b를 c로, ..., y를 z로, z를 a로 바꾸는 것을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>번 반복하는 것이다.</p>

<p>당신은 동호가 암호화한 이름이 원래 어떤 학교의 것이었는지 알고 싶으나, 동호가 고른 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>을 알지 못한다.</p>

<p>암호화된 이름이 주어졌을 때, 그 이름이 원래 어떤 학교의 이름이었는지 알아내는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 암호화된 학교의 이름이 주어진다. 모든 입력은 위에서 서술된 과정에 따라 생성되었다.</p>

### 출력 

 <p>첫 번째 줄에 암호화된 학교의 이름이 NLCS의 것이라면 <code>NLCS</code>, BHA의 것이라면 <code>BHA</code>, KIS의 것이라면 <code>KIS</code>, SJA의 것이라면 <code>SJA</code>를 출력한다.</p>

