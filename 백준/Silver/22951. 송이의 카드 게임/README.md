# [Silver V] 송이의 카드 게임 - 22951 

[문제 링크](https://www.acmicpc.net/problem/22951) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>혜민이는 오랜만에 친구들과 카드 게임을 하고 싶어졌다. 일반 카드 게임을 많이 해서 지겨웠던 혜민이는 새로운 카드 게임을 생각해냈다.</p>

<ul>
	<li>혜민이를 포함하여 $N$명이 둥글게 앉아있고 각각 $K$개의 카드를 가지고 시작한다. 이 게임을 고안해낸 혜민이부터 반시계방향으로 $N$명에게 순서대로 $1$부터 $N$까지 번호가 주어진다. 카드에는 $1$이상 $10$이하인 정수가 적혀있다.</li>
	<li>우선 자신이 가진 $K$ 개의 카드를 자기 앞의 바닥에 일렬로 내려놓는다. 이렇게 하면 총 $N \times K$ 개의 카드가 둥글게 배치된 모양이 된다. 바닥에 내려놓은 카드의 순서는 바꿀 수 없다.</li>
	<li>게임은 $1$번 사람의 제일 왼쪽에 있는 카드부터 선택하면서 시작한다. 선택된 카드는 다음과 같은 과정을 거치게 된다.
	<ul>
		<li>선택된 카드에 적힌 수 $X$를 확인한 후 카드를 제거한다.</li>
		<li>바닥에 남아있는 카드들 중, 제거된 카드의 오른쪽 $X$번째에 위치한 카드를 다시 선택한다.</li>
	</ul>
	</li>
	<li>이렇게 카드를 선택해 나가다가 마지막 한 장이 바닥에 남으면 그 카드의 주인이 승리한다.</li>
</ul>

<p>예를 들어, 3명의 사람이 각각 2개의 카드를 가지고 있을 때 1번 사람이 $9$, $5$, 2번 사람이 $1$, $2$, 3번 사람이 $3$, $10$ 이 적힌 카드를 차례대로 바닥에 내려놓은 상태를 생각해보자. 카드가 선택되는 순서는 아래와 같다.</p>

<table border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 500px;">
	<tbody>
		<tr>
			<td>
			<p style="text-align: center;"><img alt="" src="" style="height: 169px; width: 300px;"></p>

			<p style="text-align: center;">(1)</p>
			</td>
			<td style="text-align: center;">
			<p><img alt="" src="" style="height: 169px; width: 300px;"></p>

			<p>(2)</p>
			</td>
			<td style="text-align: center;">
			<p><img alt="" src="" style="height: 169px; width: 300px;"></p>

			<p>(3)</p>
			</td>
		</tr>
		<tr>
			<td style="text-align: center;">
			<p><img alt="" src="" style="height: 169px; width: 300px;"></p>

			<p>(4)</p>
			</td>
			<td style="text-align: center;">
			<p><img alt="" src="" style="height: 169px; width: 300px;"></p>

			<p>(5)</p>
			</td>
			<td style="text-align: center;">
			<p><img alt="" src="" style="height: 169px; width: 300px;"></p>

			<p>(6)</p>
			</td>
		</tr>
	</tbody>
</table>

<p>직접 고안해낸 게임이지만 지루한 걸 싫어하는 혜민이는 이 긴 과정을 기다리고 싶지 않다. 게임을 시작하자 마자 결과를 알고 싶은 혜민에게 이긴 사람의 번호와 마지막까지 남아 있는 카드의 숫자를 알려주자.</p>

### 입력 

 <p>첫 번째 줄에 사람 수 $N$($1 \leq N \leq 100$)과 각각 가져갈 카드 수 $K$($1 \leq K \leq 10$)가 주어진다. </p>

<p>두 번째 줄부터 $N+1$ 번째 줄까지 $N$개의 줄에 걸쳐서 각각의 사람이 바닥에 내려놓은 카드를 나타내는 $K$개의 정수가 주어진다.</p>

<p>$i+1$번째 줄은 $i$번 사람이 들고 있는 카드를 나타내며, 각 줄에서 $j$번째로 주어지는 정수는 왼쪽에서 $j$번째에 위치한 카드에 적힌 수를 의미한다. ($1 \leq i \leq N$, $1 \leq j \leq K$, $1 \le$ 카드에 적힌 수 $\le 10$)</p>

### 출력 

 <p>이긴 사람의 번호와 마지막까지 남아 있는 카드에 적힌 수를 공백으로 구분하여 한 줄에 출력한다.</p>

