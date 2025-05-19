# [Bronze II] 일기 암호화하기 - 33869 

[문제 링크](https://www.acmicpc.net/problem/33869) 

### 성능 요약

메모리: 108384 KB, 시간: 96 ms

### 분류

구현, 문자열

### 제출 일자

2025년 5월 19일 15:18:35

### 문제 설명

<p>송이는 매일 일기를 쓴다. 일기를 비밀스럽게 쓰고 싶어진 송이는 단어 키를 이용한 암호화를 사용하여 독서록을 작성하려고 한다.</p>

<p>단어 키를 사용한 암호화란 다음과 같다.</p>

<ol>
	<li>암호화에 사용할 단어를 고른다.</li>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>에서 선정한 단어에서 알파벳이 중복되지 않도록 추출해 단어 키를 만든다. 특정 알파벳이 여러 번 등장한다면 처음 등장한 경우를 제외하고 해당 알파벳을 버린다.</li>
	<li>암호화 표를 만든다. 암호화 표를 만드는 방법은 아래와 같다.
	<ul>
		<li>윗줄에 평문 문자인 알파벳을 순서대로 쓰고, 아랫줄에는 단어 키를 첫 번째 위치부터 순서대로 쓴다.</li>
		<li>단어 키에 속하는 문자를 제외한 알파벳의 나머지 문자를 순서대로 써서 표를 완성한다.</li>
	</ul>
	</li>
</ol>

<p>예를 들어 암호화에 사용할 단어가 <span style="color:#e74c3c;"><code><samp>THEFIFTHSMUPC</samp></code></span>라고 하면 단어 키는 <span style="color:#e74c3c;"><code>THEFISMUPC</code></span>가 되고, 암호화 표는 아래와 같이 완성된다.</p>

<table class="table table-bordered td-center th-center">
	<tbody>
		<tr>
			<td>평문</td>
			<td>A</td>
			<td>B</td>
			<td>C</td>
			<td>D</td>
			<td>E</td>
			<td>F</td>
			<td>G</td>
			<td>H</td>
			<td>I</td>
			<td>J</td>
			<td>K</td>
			<td>L</td>
			<td>M</td>
			<td>N</td>
			<td>O</td>
			<td>P</td>
			<td>Q</td>
			<td>R</td>
			<td>S</td>
			<td>T</td>
			<td>U</td>
			<td>V</td>
			<td>W</td>
			<td>X</td>
			<td>Y</td>
			<td>Z</td>
		</tr>
		<tr>
			<td>암호</td>
			<td>T</td>
			<td>H</td>
			<td>E</td>
			<td>F</td>
			<td>I</td>
			<td>S</td>
			<td>M</td>
			<td>U</td>
			<td>P</td>
			<td>C</td>
			<td>A</td>
			<td>B</td>
			<td>D</td>
			<td>G</td>
			<td>J</td>
			<td>K</td>
			<td>L</td>
			<td>N</td>
			<td>O</td>
			<td>Q</td>
			<td>R</td>
			<td>V</td>
			<td>W</td>
			<td>X</td>
			<td>Y</td>
			<td>Z</td>
		</tr>
	</tbody>
</table>

<p>암호화 표의 평문 행에 있는 알파벳을 암호화한 결과는 같은 열에 있는 암호 행의 알파벳이 된다. 위 표를 이용해 <span style="color:#e74c3c;"><code>GOODLUCK</code></span>이라는 문장을 암호화하면 <span style="color:#e74c3c;"><code>MJJFBREA</code></span>가 된다.</p>

<p>암호화에 사용할 단어 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$W$</span></mjx-container>와 암호화할 문장 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>가 주어졌을 때 문장을 암호화한 결과를 출력하자.</p>

### 입력 

 <p>첫째 줄에 공백 없이 알파벳 대문자로만 구성된 암호화에 사용할 단어 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>W</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$W$</span></mjx-container>가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mo data-mjx-texclass="OPEN" fence="false" stretchy="false">|</mo><mi>W</mi><mo data-mjx-texclass="CLOSE" fence="false" stretchy="false">|</mo><mo>≤</mo><mn>20</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq \lvert W \rvert \leq 20)$</span> </mjx-container></p>

<p>둘째 줄에 공백 없이 알파벳 대문자로만 구성된 암호화할 문장 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mo data-mjx-texclass="OPEN" fence="false" stretchy="false">|</mo><mi>S</mi><mo data-mjx-texclass="CLOSE" fence="false" stretchy="false">|</mo><mo>≤</mo><mn>200</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 \leq \lvert S \rvert \leq 200)$</span> </mjx-container></p>

### 출력 

 <p>단어 키를 이용해 문장 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>를 암호화한 결과를 출력한다.</p>

