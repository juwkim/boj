# [Bronze I] SMUPC NAME - 31859 

[문제 링크](https://www.acmicpc.net/problem/31859) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

구현, 문자열

### 제출 일자

2024년 5월 19일 22:29:03

### 문제 설명

<p>연재는 제4회 SMUPC에 출전하는 사람들을 위해 <strong>SMUPC NAME</strong>을 만들어주려고 한다. <strong>SMUPC NAME</strong>을 만드는 방법은 아래와 같다.</p>

<ol>
	<li>출전자의 영어 이름에서 알파벳이 중복되지 않도록 추출한다. 특정 알파벳이 여러 번 등장한다면 처음 등장한 경우를 제외하고 해당 알파벳을 버린다.</li>
	<li>1번을 통해 만들어진 문자열 맨 뒤에 1번 과정에서 버려진 문자의 총개수에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>를 더한 값을 붙인다.</li>
	<li>2번을 통해 만들어진 문자열 맨 앞에 출전 등록 번호에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1906</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1906$</span></mjx-container>을 더한 값을 붙인다.</li>
	<li>3번을 통해 만들어진 문자열을 뒤집는다.</li>
	<li>4번을 통해 만들어진 문자열 맨 앞에 "<code><span style="color:#e74c3c;">smupc_</span></code>"를 붙인다.</li>
</ol>

<p>출전 등록 번호가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2$</span></mjx-container>이며 "<span style="color:#e74c3c;"><code>yeonjaechoi</code></span>" 라는 영어 이름을 가진 사람의 <strong>SMUPC NAME</strong>을 규칙에 따라 만들면 다음과 같다.</p>

<ol>
	<li>yeonjachi</li>
	<li>yeonjachi6</li>
	<li>1908yeonjachi6</li>
	<li>6ihcajnoey8091</li>
	<li>smupc_6ihcajnoey8091</li>
</ol>

<p>출전 등록 번호와 영어 이름이 주어지면 그 사람의 <strong>SMUPC NAME</strong>을 출력하자.</p>

### 입력 

 <p>첫째 줄에 출전 등록 번호 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N (1 \leq N \leq 100)$</span></mjx-container>과 공백 없이 알파벳 소문자로만 구성된 영어 이름 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mo data-mjx-texclass="OPEN" fence="false" stretchy="false">|</mo><mi>S</mi><mo data-mjx-texclass="CLOSE" fence="false" stretchy="false">|</mo><mo>≤</mo><mn>20</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S (1 \leq \lvert S \rvert \leq 20)$</span></mjx-container>가 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>규칙에 따라 만든 <strong>SMUPC NAME</strong>을 출력한다.</p>

