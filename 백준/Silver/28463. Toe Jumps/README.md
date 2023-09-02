# [Silver V] Toe Jumps - 28463 

[문제 링크](https://www.acmicpc.net/problem/28463) 

### 성능 요약

메모리: 113112 KB, 시간: 128 ms

### 분류

많은 조건 분기, 구현

### 문제 설명

<p align="left" style="text-align:left; margin-bottom:11px">피겨 스케이팅에는 악셀, 러츠, 플립, 룹, 살코, 토룹으로 총 6가지의 점프가 있다. 점프는 토(Toe) 계열 점프와 에지(Edge) 계열 점프로 나눌 수 있다. 점프 시에 토를 빙판에 찍는 점프를 토 계열 점프라 하고, 토 계열 점프에는 토룹, 플립, 러츠가 있다. 아래는 오른발잡이 선수를 기준으로 남쪽(<span style="color:#e74c3c;"><code>S</code></span>)으로 진행할 때, 토 계열 점프 시 빙판에 남는 자취를 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>×</mo><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2\times2$</span></mjx-container> 격자판으로 표현한 것이다.</p>

<p style="margin-bottom: 11px; text-align: center;">진행 방향: ↓ (남쪽, <span style="color:#e74c3c;"><code>S</code></span>)</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 100px; height: 100px;">
	<caption>토룹(T)</caption>
	<tbody>
		<tr>
			<td style="text-align: center;"><code>.</code></td>
			<td style="text-align: center;"><code>O</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>P</code></td>
			<td style="text-align: center;"><code>.</code></td>
		</tr>
	</tbody>
</table>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="height: 100px; width: 100px;">
	<caption>플립(F)</caption>
	<tbody>
		<tr>
			<td style="text-align: center;"><code>I</code></td>
			<td style="text-align: center;"><code>.</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>.</code></td>
			<td style="text-align: center;"><code>P</code></td>
		</tr>
	</tbody>
</table>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="height: 100px; width: 100px;">
	<caption>러츠(Lz)</caption>
	<tbody>
		<tr>
			<td style="text-align: center;"><code>O</code></td>
			<td style="text-align: center;"><code>.</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>.</code></td>
			<td style="text-align: center;"><code>P</code></td>
		</tr>
	</tbody>
</table>

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>×</mo><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2\times2$</span></mjx-container> 격자판의 자취와 진행 방향이 주어졌을 때, 각 점프가 어떤 토 계열의 점프인지 출력하시오. 진행 방향은 ‘<span style="color:#e74c3c;"><code>E</code></span>’, ‘<span style="color:#e74c3c;"><code>W</code></span>’, ‘<span style="color:#e74c3c;"><code>S</code></span>’, ‘<span style="color:#e74c3c;"><code>N</code></span>’ 한 글자의 문자로 주어지며 각각 동, 서, 남, 북 방향으로 진행함을 의미한다.</p>

### 입력 

 <p>첫째 줄에는 진행 방향을 나타내는 알파벳 대문자 ‘<span style="color:#e74c3c;"><code>E</code></span>’, ‘<span style="color:#e74c3c;"><code>W</code></span>’, ‘<span style="color:#e74c3c;"><code>S</code></span>’, ‘<span style="color:#e74c3c;"><code>N</code></span>’ 중 하나가 주어진다.</p>

<p>다음 두 개의 줄에 거쳐 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>×</mo><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2\times2$</span></mjx-container> 격자판이 주어진다. 격자판은 오직 ‘<span style="color:#e74c3c;"><code>.</code></span>’, ‘<span style="color:#e74c3c;"><code>I</code></span>’, ‘<span style="color:#e74c3c;"><code>O</code></span>’, ‘<span style="color:#e74c3c;"><code>P</code></span>’로만 이루어져 있다.</p>

### 출력 

 <p>첫째 줄에 어떤 토 계열의 점프인지 출력한다.</p>

<p>토룹은 “<span style="color:#e74c3c;"><code>T</code></span>”, 플립은 “<span style="color:#e74c3c;"><code>F</code></span>”, 러츠는 “<span style="color:#e74c3c;"><code>Lz</code></span>”를 출력하고, 어떤 토 점프도 아니면 “<span style="color:#e74c3c;"><code>?</code></span>”를 출력한다.</p>

