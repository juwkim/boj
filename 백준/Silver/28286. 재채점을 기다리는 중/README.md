# [Silver II] 재채점을 기다리는 중 - 28286 

[문제 링크](https://www.acmicpc.net/problem/28286) 

### 성능 요약

메모리: 111472 KB, 시간: 180 ms

### 분류

백트래킹, 브루트포스 알고리즘, 구현

### 제출 일자

2024년 12월 10일 22:39:13

### 문제 설명

<p>UCPC고등학교에 다니는 민규는 최근에 기말고사를 치게 되었다. 기말고사는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>문제로 이루어져 있고, 각 문제는 보기가 1 이상 5 이하의 정수로 이루어진 객관식 문제이다.</p>

<p>시간이 지나 학교에서 성적표를 받은 민규는 집에서 매겨본 점수보다 훨씬 낮은 점수를 받고 깜짝 놀랐다. 알고 보니 민규는 OMR 카드에 답안을 밀려 썼던 것이다. 억울하지만 어쩔 수 없이 결과를 받아들여야 했던 민규는 자신이 답안을 제대로 썼다면 얼마나 잘 봤을지라도 알아보기로 했다.</p>

<p>민규는 OMR 카드에 쓴 답안을 밀거나 당기는 작업을 최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>번 할 수 있다. 답안을 한 번 밀거나 당기려면 우선 기준점이 될 문제의 번호 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$p$</span></mjx-container>를 하나 잡고, 다음 중 하나를 시행한다.</p>

<ul>
	<li>당기기: <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$p$</span></mjx-container>번 문제의 뒤 문제들에 쓴 답안을 모두 직전 문제로 옮기고, 마지막 문제는 답안을 쓰지 않은 것으로 취급한다.</li>
	<li>밀기: <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$p$</span></mjx-container>번 및 그 뒤의 문제들에 쓴 답안을 모두 직후 문제로 옮기고, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$p$</span></mjx-container>번 문제는 답안을 쓰지 않은 것으로 취급한다. 마지막 문제에 쓴 답안은 버린다.</li>
</ul>

<p>다음은 3번 문제를 기준으로 답안을 밀거나 당기는 예시이다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 500px;">
	<thead>
		<tr>
			<th scope="col" style="text-align: center;">문제번호</th>
			<th scope="col" style="text-align: center;">1</th>
			<th scope="col" style="text-align: center;">2</th>
			<th scope="col" style="text-align: center;">3</th>
			<th scope="col" style="text-align: center;">4</th>
			<th scope="col" style="text-align: center;">5</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align: center;">OMR카드 원본</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;">1</td>
		</tr>
		<tr>
			<td style="text-align: center;">당기기</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">.</td>
		</tr>
		<tr>
			<td style="text-align: center;">밀기</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">.</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">5</td>
		</tr>
	</tbody>
</table>

<p>기준점의 번호는 매 작업마다 달라도 된다.</p>

<p>답안을 밀거나 당기는 작업을 최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>번 실행한 후 민규가 맞힐 수 있는 문제의 최대 개수를 구하시오. 작업을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>번보다 적게 하거나 아예 안 할 수도 있음에 유의하여라.</p>

### 입력 

 <p>첫 줄에 문제 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>과 답안을 밀거나 당길 수 있는 최대 횟수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$K$</span></mjx-container>가 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>5</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(5 \le N \le 20$</span></mjx-container>; <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D43E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>K</mi><mo>≤</mo><mn>3</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le K \le 3)$</span> </mjx-container></p>

<p>그 다음 줄에 각 문제의 정답을 나타내는 1 이상 5 이하의 정수가 차례대로 주어진다.</p>

<p>그 다음 줄에 민규가 OMR 카드에 기입한 답안을 나타내는 1 이상 5 이하의 정수가 차례대로 주어진다.</p>

### 출력 

 <p>민규가 맞힐 수 있는 문제의 최대 개수를 출력한다.</p>

