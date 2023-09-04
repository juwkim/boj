# [Bronze II] 학점계산프로그램 - 29614 

[문제 링크](https://www.acmicpc.net/problem/29614) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

사칙연산, 구현, 수학, 문자열

### 문제 설명

<p>종현은 영도와 함께 학교 포털 사이트에서 데이터를 가져와 본인의 학점을 계산하는 프로그램을 만들고 있다. 종현은 영도가 사이트에서 추출한 등급 데이터를 사용해서 평균 학점을 출력하고자 한다. </p>

<p>등급별 학점은 다음의 표를 따른다.</p>

<table class="table table-bordered table-center-30">
	<tbody>
		<tr>
			<td style="text-align: center;">등급</td>
			<td style="text-align: center;">학점</td>
		</tr>
		<tr>
			<td style="text-align: center;">A+</td>
			<td style="text-align: center;">4.5</td>
		</tr>
		<tr>
			<td style="text-align: center;">A</td>
			<td style="text-align: center;">4.0</td>
		</tr>
		<tr>
			<td style="text-align: center;">B+</td>
			<td style="text-align: center;">3.5</td>
		</tr>
		<tr>
			<td style="text-align: center;">B</td>
			<td style="text-align: center;">3.0</td>
		</tr>
		<tr>
			<td style="text-align: center;">C+</td>
			<td style="text-align: center;">2.5</td>
		</tr>
		<tr>
			<td style="text-align: center;">C</td>
			<td style="text-align: center;">2.0</td>
		</tr>
		<tr>
			<td style="text-align: center;">D+</td>
			<td style="text-align: center;">1.5</td>
		</tr>
		<tr>
			<td style="text-align: center;">D</td>
			<td style="text-align: center;">1.0</td>
		</tr>
		<tr>
			<td style="text-align: center;">F</td>
			<td style="text-align: center;">0.0</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫째 줄에 과목별 등급이 나열된 문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>가 주어진다. 등급 사이에는 별도의 구분자가 없다. 문자열은 표에 있는 문자들로만 이루어져 있으며, 최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\,000$</span></mjx-container> 글자로 이루어져 있다.</p>

### 출력 

 <p>문자열 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>S</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$S$</span></mjx-container>에 나열된 등급으로 구한 학점의 산술평균을 첫째 줄에 출력한다. 정답과 출력값의 절대/상대 오차는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mo>−</mo><mn>4</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^{-4}$</span></mjx-container>까지 허용한다.</p>

