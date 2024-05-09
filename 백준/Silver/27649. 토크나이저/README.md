# [Silver III] 토크나이저 - 27649 

[문제 링크](https://www.acmicpc.net/problem/27649) 

### 성능 요약

메모리: 3920 KB, 시간: 8 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2024년 5월 10일 08:14:53

### 문제 설명

<p>주원이는 시스템과 상호 작용할 수 있는 편리한 텍스트 인터페이스를 제공하는 셸을 만들고 있습니다. 셸은 명령문을 입력받으면, 차례로 tokenizer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">→</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\rightarrow$</span></mjx-container> lexer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">→</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\rightarrow$</span></mjx-container> parser <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">→</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\rightarrow$</span></mjx-container> expander <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2192"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">→</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\rightarrow$</span></mjx-container> executor를 호출하여 명령문을 해석하고, 유효한 프로그램을 실행합니다. 주원이는 셸을 만들기 위해 가장 먼저 아래의 구분자들로 명령문을 자르는 토크나이저를 개발해야 합니다. 하지만 문자열은 항상 공백으로만 구분해 왔던 주원이는 여러 구분자로 명령문을 자르는 것을 어려워하고 있습니다. 주원이의 멋진 셸을 위하여 토크나이저를 만드는 것을 도와주세요.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td style="text-align: center;">구분자</td>
			<td style="text-align: center;">명령문</td>
			<td style="text-align: center;">출력 예시</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code><</code></td>
			<td style="text-align: center;"><code>cat <infile</code></td>
			<td style="text-align: center;"><code>cat < infile</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>></code></td>
			<td style="text-align: center;"><code>program >outfile</code></td>
			<td style="text-align: center;"><code>program > outfile</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>&&</code></td>
			<td style="text-align: center;"><code>program&&echo success</code></td>
			<td style="text-align: center;"><code>program && echo success</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>||</code></td>
			<td style="text-align: center;"><code>grep sol < for||echo fail</code></td>
			<td style="text-align: center;"><code>grep sol < for || echo fail</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>(</code></td>
			<td style="text-align: center;"><code>(exit 0)</code></td>
			<td style="text-align: center;"><code>( exit 0 )</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>)</code></td>
			<td style="text-align: center;"><code>(cd $OLDPWD ) && pwd</code></td>
			<td style="text-align: center;"><code>( cd $OLDPWD ) && pwd</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>" " (공백)</code></td>
			<td style="text-align: center;"><code>echo 1  2   3    4</code></td>
			<td style="text-align: center;">
			<p><code>echo 1 2 3 4</code></p>
			</td>
		</tr>
	</tbody>
</table>

<p>토크나이저는 다음과 같은 방식으로 동작한다.</p>

<ol>
	<li>문자열을 앞에서부터 읽어나간다.</li>
	<li>구분자를 만나면 구분자의 앞뒤를 자른다. 이후 구분자의 다음 위치부터 다시 읽어나간다. 이때 잘린 문자열을 토큰이라고 한다.</li>
	<li>문자열의 끝에 도달할 경우, 앞에서부터 차례대로 토큰들을 공백으로 구분하여 출력한다. 단, 토큰이 공백일 경우 출력하지 않는다.</li>
</ol>

<p>문자열 S를 <code>"grep skku   <infile> outfile"</code>라고 하자. 이때 토큰을 <strong><span style="color:#c0392b;">:</span></strong> 을 기준으로 구분할 때 문자열 S는 아래와 같이 토큰화된다.</p>

<p><code>grep<strong><span style="color:#c0392b;">: </span></strong><strong><span style="color:#c0392b;">:</span></strong>skku<strong><span style="color:#c0392b;">: : : :</span></strong><<strong><span style="color:#c0392b;">:</span></strong>infile<span style="font-weight: bold; color: rgb(192, 57, 43);">:</span>><strong><span style="color:#c0392b;">: </span></strong><span style="font-weight: bold; color: rgb(192, 57, 43);">:</span>outfile</code></p>

<p>위 토큰 중 단일 공백으로만 이루어진 토큰을 제외하여 순서대로 공백으로 구분하여 출력한다. 예시의 경우 <code>"grep skku < infile > outfile"</code>를 출력한다.</p>

### 입력 

 <p>첫째 줄에 셸 명령문 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>가 주어집니다. 명령문은 구분자와 알파벳 대소문자, 숫자 및 $, ?, +, _로 이루어져 있습니다. <strong>& 또는 |가 홀수 번 연속으로 주어지지 않습니다.</strong> <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mi>S</mi><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(|S|\le1\,000\,000)$</span> </mjx-container></p>

### 출력 

 <p>셸 명령문 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>를 구분자를 기준으로 토큰화하세요. <strong>이때 단일 공백으로만 이루어진 토큰을 제외한 </strong>토큰들을 단일 공백으로 구분하여 출력하세요.</p>

