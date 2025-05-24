# [Silver V] 불필요한 for문 - 33904 

[문제 링크](https://www.acmicpc.net/problem/33904) 

### 성능 요약

메모리: 108896 KB, 시간: 88 ms

### 분류

구현, 문자열

### 제출 일자

2025년 5월 24일 23:06:06

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/1524a739-a27f-45e0-80c0-a027fe00dc9b/-/preview/" style="width: 410px; height: 160px;"></p>

<p>준호는 최근 백준 문제를 풀던 중 실수로 변수명을 잘못 써서 코드에 불필요한 for문이 있음에도 맞았습니다를 받았다!</p>

<p>처음 겪어보는 상황에 준호는 혹시 전에 제출했던 코드에도 불필요한 for문이 있지 않았을까? 생각하고 과거에 제출했던 코드들을 살펴보기로 했다.</p>

<p>입력으로 주어질 코드의 형식은 다음과 같다.</p>

<ul>
	<li>코드는 한 줄 이상의 for문과 마지막 한 줄의 연산식으로 이루어져 있다.</li>
	<li>for문을 구성하는 각 줄은 <code>for (int [변수명] = 1; [변수명] < 9; [변수명]++)</code> 의 형식으로 주어진다. 이는 [변수명]이라는 변수를 선언한 것이며, 세 [변수명]은 동일하다.</li>
	<li>변수명은 알파벳 한 글자이며, 대소문자를 구분한다. 즉, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>과 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>은 다른 변수이다.</li>
	<li>연산식은 알파벳, 숫자, 공백, 특수문자(아스키코드 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>32</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$32$</span></mjx-container>-<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>126</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$126$</span></mjx-container>)로 이루어져 있고, 공백으로 시작/끝나지 않는 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container> 이하의 문자열이다.</li>
	<li>연산식의 알파벳들은 반드시 변수명만을 의미하며 알파벳이 연속으로 주어지지 않는다.</li>
	<li>연산식은 실제 프로그래밍 코드 형식과는 무관하다. 또한 선언되지 않은 변수가 사용될 수 있다.</li>
</ul>

<p>여기서 불필요한 for문이란 다음 두 가지 조건 중 하나라도 만족하는 for문을 말한다.</p>

<ul>
	<li>해당 for문에서 선언한 변수가 내부의 다른 for문에서 다시 선언된 경우</li>
	<li>해당 for문에서 선언한 변수가 연산식에서 전혀 사용되지 않은 경우</li>
</ul>

<p>준호의 코드가 주어지면 불필요한 for문들을 모두 제거한 코드를 출력하자!</p>

### 입력 

 <p>여러 줄에 걸쳐 준호의 코드가 주어진다. 코드는 최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>500</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$500$</span></mjx-container>줄이다.</p>

<p>두 번째 줄부터는 코드의 앞에 한 줄에 하나씩 공백(space) 문자가 추가된다.</p>

### 출력 

 <p>여러 줄에 걸쳐 준호의 코드에서 불필요한 for문에 해당하는 행을 모두 지운 코드를 출력한다.</p>

<p>두 번째 줄부터는 코드의 앞에 한 줄에 하나씩 공백(space) 문자를 추가한다.</p>

