# [Bronze IV] 강당 대관 - 31994 

[문제 링크](https://www.acmicpc.net/problem/31994) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

구현

### 제출 일자

2024년 6월 19일 11:02:23

### 문제 설명

<p>한국정보기술진흥원에서는 다양한 세미나가 열린다.</p>

<p>전문가를 위한 알고리즘, 데이터분석, 인공지능, 사이버보안, 네트워크 세미나뿐만 아니라 예비 창업가를 위한 창업 세미나, 그리고 청소년들을 위한 입시 세미나가 열린다</p>

<table class="table table-bordered table-center-30 th-center td-center">
	<tbody>
		<tr>
			<th>세미나</th>
		</tr>
		<tr>
			<td>Algorithm</td>
		</tr>
		<tr>
			<td>DataAnalysis</td>
		</tr>
		<tr>
			<td>ArtificialIntelligence</td>
		</tr>
		<tr>
			<td>CyberSecurity</td>
		</tr>
		<tr>
			<td>Network</td>
		</tr>
		<tr>
			<td>Startup</td>
		</tr>
		<tr>
			<td>TestStrategy</td>
		</tr>
	</tbody>
</table>

<p>오늘은 위 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$7$</span></mjx-container>개 주제의 세미나가 모두 열리는 날이다. 가장 많은 신청자 수를 가진 세미나에게 대강당을 대관해준다고 할 때, 대강당을 사용하는 세미나의 이름을 구하자.</p>

### 입력 

 <p><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$7$</span></mjx-container>줄에 걸쳐서 세미나의 이름과 신청자 수가 공백으로 구분되어 주어진다.</p>

<p>세미나는 지문의 표에 있는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$7$</span></mjx-container>개이며, 중복 되는 세미나는 주어지지 않는다.</p>

<p>신청자 수는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container> 이하의 정수로만 주어지며, 신청자 수는 중복으로 주어지지 않는다.</p>

### 출력 

 <p>첫 번째 줄에 대강당을 사용하는 세미나의 이름을 출력한다.</p>

