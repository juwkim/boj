# [Bronze II] 카트라이더: 드리프트 - 27522 

[문제 링크](https://www.acmicpc.net/problem/27522) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation), 정렬(sorting), 문자열(string)

### 문제 설명

<p><em>카트라이더: 드리프트 </em>는 2023년 1월 12일에 출시한 넥슨의 캐주얼 레이싱 게임으로, 2004년에 출시하여 18년간 서비스한 <em>크레이지레이싱 카트라이더 </em>의 후속작이다. PC-콘솔-모바일의 크로스 플랫폼 플레이를 지원하며, 커스터마이징을 통해 나만의 카트바디와 개성 있는 캐릭터를 사용할 수 있는 것이 특징이다. 특히 기존 <em>카트라이더 </em>의 게임성을 계승하면서 더욱 뛰어난 그래픽을 자랑한다는 점에서 많은 관심을 받고 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6f58a183-4600-4a46-bacf-0a4bb5a33223/-/preview/" style="height: 281px; width: 500px;"></p>

<p style="text-align: center;">그림 1. <em>카트라이더: 드리프트</em></p>

<p><em>카트라이더: 드리프트 </em>에는 크게 아이템전과 스피드전의 두 가지 모드가 있다. 아이템전은 다양한 아이템을 사용할 수 있는 모드로, 팀의 협동을 통한 전략적 플레이가 핵심이다. 반면 스피드전은 드리프트를 통해 부스터를 모아 사용하는 모드로, 짜릿한 속도감을 즐길 수 있다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 550px;">
	<tbody>
		<tr>
			<td style="text-align: center; vertical-align: middle; width: 275px;"><img alt="" src="https://upload.acmicpc.net/ba882598-d3dc-49d2-a290-6e50e490fa23/-/preview/" style="height: 208px; width: 300px;"></td>
			<td style="text-align: center; vertical-align: middle; width: 275px;">
			<p><img alt="" src="https://upload.acmicpc.net/5e15f25a-371a-4008-9d1c-7fe4d6ea112f/-/preview/" style="height: 182px; width: 330px;"></p>
			</td>
		</tr>
		<tr>
			<td style="text-align: center; vertical-align: middle; width: 275px;">그림 2. <em>카트라이더: 드리프트 </em>의 아이템전</td>
			<td style="text-align: center; vertical-align: middle; width: 275px;">그림 3. <em>카트라이더: 드리프트 </em>의 스피드전</td>
		</tr>
	</tbody>
</table>

<p>당신은 스피드전 스쿼드의 승리 팀을 구하는 임무를 맡았다. 스쿼드는 레드팀 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>명과 블루팀 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>명으로 이루어진 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8$</span></mjx-container>명의 레이서가 플레이하는 모드이다. 또한 스피드전에서는 각 팀원의 순위 점수의 합계가 높은 팀이 승리하며, 만일 합계가 같다면 최고 순위가 가장 높은 팀이 승리한다. 참고로 아래 순위 점수표를 확인해보면, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8$</span></mjx-container>명의 레이서가 모두 서로 다른 시각에 완주한 경우 순위 점수의 합계가 반드시 다르다.</p>

<p>원래 1위 레이서가 완주한 순간부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10$</span></mjx-container>초가 지나기 전에 완주하지 못하면 리타이어되지만, 이 문제에서는 모든 레이서의 실력이 뛰어나기 때문에 아무도 리타이어하지 않는다. 또한 모든 레이서가 반드시 서로 다른 시각에 완주한다. 스피드전 스쿼드에 참가한 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8$</span></mjx-container>명의 레이서에 대해 완주 기록과 속한 팀이 주어졌을 때, 아래 순위 점수표를 참고하여 승리팀이 어디인지 판단해보자.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 600px;" summary="카트라이더: 드리프트 순위 점수 표">
	<caption>표 1. <em>카트라이더: 드리프트</em> 스피드전 순위 점수</caption>
	<tbody>
		<tr>
			<td style="text-align: center; vertical-align: middle; width: 60px;">순위</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">1st</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">2nd</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">3rd</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">4th</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">5th</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">6th</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">7th</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">8th</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">Retire</td>
		</tr>
		<tr>
			<td style="text-align: center; vertical-align: middle; width: 60px;">점수</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">10</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">8</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">6</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">5</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">4</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">3</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">2</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">1</td>
			<td style="text-align: center; vertical-align: middle; width: 60px;">0</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8$</span></mjx-container>개의 줄에 걸쳐 한 줄에 한 명씩 각 레이서의 완주 기록과 속한 팀이 공백을 사이에 두고 주어진다.</p>

<ul>
	<li>레이서의 완주 기록은 <span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color:#e95849;"><code>M:SS:sss</code></span>와 같은 형식으로 주어진다.</li>
	<li>분(<span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color:#e95849;"><code>M</code></span>)은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9$</span></mjx-container> 이하의 정수, 초(<span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color:#e95849;"><code>SS</code></span>)는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>59</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$59$</span></mjx-container> 이하의 정수, 밀리초(<span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color:#e95849;"><code>sss</code></span>)는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>999</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$999$</span></mjx-container> 이하의 정수로 자릿수가 부족한 경우 앞에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>을 붙여 나타낸다.</li>
	<li>모든 레이서는 <code>0:00:001</code> 이상 <code>9:59:999</code> 이하의 서로 다른 시각에 완주한다. 리타이어가 발생하지 않는 입력만 주어진다.</li>
	<li>레이서가 속한 팀은 레드팀인 경우 <span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color:#e95849;"><code>R</code></span>, 블루팀인 경우 <span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color:#e95849;"><code>B</code></span>로 주어진다.</li>
</ul>

### 출력 

 <p>레드팀이 승리하였다면 <span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color:#e95849;"><code>Red</code></span>를, 블루팀이 승리하였다면 <span data-darkreader-inline-color="" style="color: rgb(231, 76, 60); --darkreader-inline-color:#e95849;"><code>Blue</code></span>를 출력한다.</p>

