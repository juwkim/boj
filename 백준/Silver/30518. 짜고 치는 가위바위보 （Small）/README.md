# [Silver I] 짜고 치는 가위바위보 (Small) - 30518 

[문제 링크](https://www.acmicpc.net/problem/30518) 

### 성능 요약

메모리: 111484 KB, 시간: 688 ms

### 분류

백트래킹, 브루트포스 알고리즘

### 제출 일자

2025년 4월 13일 00:53:03

### 문제 설명

<p><strong>Small 버전에서는 문자열의 길이 제한이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container>으로 주어진다.</strong></p>

<p>가위바위보 챔피언십이 열렸다. 수많은 관중이 지켜보고 있다. 이 상황에서 <span style="color:#e74c3c;">lighter</span>와 <span style="color:#2980b9;">smallant</span>는 가위바위보 챔피언십 결승에 도달했다. 하지만 둘은 어릴 적부터 너무 친한 친구라, 누가 이기든 별로 신경 쓰지 않는다. 따라서 두 사람은 이번 결승에서 재미있는 장난을 치려고 한다.</p>

<p>결승전은 여러 라운드의 가위바위보로 진행된다. <span style="color:#e74c3c;">lighter</span>는 첫 번째 라운드를 제외하고, <span style="color:#2980b9;">smallant</span>가 바로 이전 라운드에 냈던 것을 따라 내는 장난을 치고자 한다. 하지만, 이런 장난은 관중이 정말 싫어한다. <span style="color:#e74c3c;">lighter</span>가 이긴 뒤 직후 라운드에서 비기는 결과가 나온다면, 관중은 두 사람이 장난을 친다는 사실을 알아채서 분노할 것이다.</p>

<p>관중이 분노하면 챔피언십의 후원이 끊길 수도 있기 때문에, <span style="color:#2980b9;">smallant</span>는 앞에 무엇을 낼지를 다시 생각해볼 필요가 있었다. 곰곰이 생각한 <span style="color:#2980b9;">smallant</span>는 기존에 내고자 했던 가위바위보의 정보 중 <strong>일부분만 취하면</strong> 문제가 해결됨을 알았다.</p>

<p>일부분만 취한다는 뜻은 기존에 내고자 했던 가위바위보의 정보가 문자열로 주어졌을 때, 그중 몇 개의 문자를 제거하여 순서를 바꾸지 않고 합치는 것을 의미한다.</p>

<p>예를 들어, 결승이 8라운드로 구성되었다고 해보자. <span style="color:#2980b9;">smallant</span>는 첫 번째 라운드부터 여덟 번째 라운드까지 <strong><표 1></strong>에 나온 것과 같이 낸다고 하자. 즉, <strong>보, 가위, 보, 가위, 보, 보, 주먹, 가위</strong> 순으로 낼 것이다. 이때 <span style="color:#e74c3c;">lighter</span>는 첫 번째 라운드만 주먹을 내고 그 이후 라운드부터는 <span style="color:#2980b9;">smallant</span>를 따라 낸다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 500px;">
	<caption><strong><표 1></strong></caption>
	<tbody>
		<tr>
			<td style="text-align: center;"><strong>라운드</strong></td>
			<td style="text-align: center;"><span style="color:#e74c3c;"><strong>lighter</strong></span></td>
			<td style="text-align: center;"><span style="color:#2980b9;"><strong>smallant</strong></span></td>
			<td style="text-align: center;"><strong>승자</strong></td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">주먹</td>
			<td style="text-align: center;">보</td>
			<td style="text-align: center;"><span style="color:#2980b9;">smallant</span></td>
		</tr>
		<tr>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">보</td>
			<td style="text-align: center;">가위</td>
			<td style="text-align: center;"><span style="color:#2980b9;">smallant</span></td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">가위</td>
			<td style="text-align: center;">보</td>
			<td style="text-align: center;"><span style="color:#e74c3c;">lighter</span></td>
		</tr>
		<tr>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">보</td>
			<td style="text-align: center;">가위</td>
			<td style="text-align: center;"><span style="color:#2980b9;">smallant</span></td>
		</tr>
		<tr>
			<td style="text-align: center;"><strong>5</strong></td>
			<td style="text-align: center;"><strong>가위</strong></td>
			<td style="text-align: center;"><strong>보</strong></td>
			<td style="text-align: center;"><strong><span style="color:#e74c3c;">lighter</span></strong></td>
		</tr>
		<tr>
			<td style="text-align: center;"><strong>6</strong></td>
			<td style="text-align: center;"><strong>보</strong></td>
			<td style="text-align: center;"><strong>보</strong></td>
			<td style="text-align: center;"><strong>무승부</strong></td>
		</tr>
		<tr>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">보</td>
			<td style="text-align: center;">주먹</td>
			<td style="text-align: center;"><span style="color:#e74c3c;">lighter</span></td>
		</tr>
		<tr>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;">주먹</td>
			<td style="text-align: center;">가위</td>
			<td style="text-align: center;"><span style="color:#e74c3c;">lighter</span></td>
		</tr>
	</tbody>
</table>

<p>이 경우, 다섯 번째 라운드에서 <span style="color:#e74c3c;">lighter</span>가 이기고 그 직후 라운드에 비겼으므로, 관중이 분노할 것이다.</p>

<p>따라서, 이 경우는 <strong><표 2></strong>와 같이 <span style="color:#2980b9;">smallant</span>가 기존에 내고자 했던 <strong>보, 가위, 보, 가위, 보, 보, 주먹, 가위</strong>의 순서에서, 여섯 번째와 일곱 번째를 제외한 <strong>보, 가위, 보, 가위, 보, 가위</strong>의 순서로 결승을 진행하면 된다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 500px;">
	<caption><strong><표 2></strong></caption>
	<tbody>
		<tr>
			<td style="text-align: center;"><strong>라운드</strong></td>
			<td style="text-align: center;"><span style="color:#e74c3c;"><strong>lighter</strong></span></td>
			<td style="text-align: center;"><span style="color:#2980b9;"><strong>smallant</strong></span></td>
			<td style="text-align: center;"><strong>승자</strong></td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">주먹</td>
			<td style="text-align: center;">보</td>
			<td style="text-align: center;"><span style="color:#2980b9;">smallant</span></td>
		</tr>
		<tr>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">보</td>
			<td style="text-align: center;">가위</td>
			<td style="text-align: center;"><span style="color:#2980b9;">smallant</span></td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">가위</td>
			<td style="text-align: center;">보</td>
			<td style="text-align: center;"><span style="color:#e74c3c;">lighter</span></td>
		</tr>
		<tr>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">보</td>
			<td style="text-align: center;">가위</td>
			<td style="text-align: center;"><span style="color:#2980b9;">smallant</span></td>
		</tr>
		<tr>
			<td style="text-align: center;"><strong>5</strong></td>
			<td style="text-align: center;"><strong>가위</strong></td>
			<td style="text-align: center;"><strong>보</strong></td>
			<td style="text-align: center;"><strong><span style="color:#e74c3c;">lighter</span></strong></td>
		</tr>
		<tr>
			<td style="text-align: center;"><strong>6</strong></td>
			<td style="text-align: center;"><strong>보</strong></td>
			<td style="text-align: center;"><strong>가위</strong></td>
			<td style="text-align: center;"><span style="color:#2980b9;"><strong>smallant</strong></span></td>
		</tr>
	</tbody>
</table>

<p><span style="color:#2980b9;">smallant</span>가 내고자 했던 가위바위보의 정보가 주어졌을 때, 관중이 분노하지 않도록 <span style="color:#2980b9;">smallant</span>가 내고자 했던 가위바위보의 정보를 <strong>일부분만 취하는</strong> 경우의 수를 구해보자. <strong>단, 최소 하나의 라운드는 존재해야 한다.</strong></p>

### 입력 

 <p><span style="color:#e74c3c;"><code>R</code></span>은 바위를, <span style="color:#e74c3c;"><code>P</code></span>는 보를, <span style="color:#e74c3c;"><code>S</code></span>는 가위를 의미한다.</p>

<p>첫 번째 줄에는 <span style="color:#e74c3c;">lighter</span>가 첫 번째 라운드에서 무엇을 낼지에 대한 정보가 알파벳 대문자 <span style="color:#e74c3c;"><code>R</code></span> 또는 <span style="color:#e74c3c;"><code>P</code></span> 또는 <span style="color:#e74c3c;"><code>S</code></span>로 주어진다.</p>

<p>두 번째 줄에는 <span style="color:#2980b9;">smallant</span>가 결승에서 무엇을 낼지에 대한 정보가 <span style="color:#e74c3c;"><code>R</code></span> 또는 <span style="color:#e74c3c;"><code>P</code></span> 또는 <span style="color:#e74c3c;"><code>S</code></span>로 구성된 길이가 <strong><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20$</span></mjx-container> 이하</strong>인 문자열로 주어진다.</p>

### 출력 

 <p>관중이 분노하지 않도록 <span style="color:#2980b9;">smallant</span>가 내고자 했던 가위바위보의 정보를 일부분만 취하는 경우의 수를 소수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-cA0"></mjx-c></mjx-mtext><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-cA0"></mjx-c></mjx-mtext><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-cA0"></mjx-c></mjx-mtext><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c37"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mtext> </mtext><mn>000</mn><mtext> </mtext><mn>000</mn><mtext> </mtext><mn>007</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\ 000\ 000\ 007$</span></mjx-container>로 나눈 나머지를 출력한다.</p>

