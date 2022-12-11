# [Silver IV] 자전거 묘기 - 25706 

[문제 링크](https://www.acmicpc.net/problem/25706) 

### 성능 요약

메모리: 148076 KB, 시간: 200 ms

### 분류

다이나믹 프로그래밍(dp)

### 문제 설명

<p>길이가 <em>N</em>미터인 직선 자전거 도로가 있다. 도로는 길이가 1미터인 <em>N</em>개의 칸으로 구분되어 있고, 가장 왼쪽에 있는 칸부터 순서대로 1번 칸, 2번 칸, …, <em>N</em>번 칸이다.</p>

<p>도로의 각 칸에는 점프대가 설치되어 있을 수 있다. <em>i(1 ≤ i ≤ N)</em>번 칸에 설치된 점프대의 높이를 <em>h<sub>i</sub></em>라고 하자. 높이가 <em>h<sub>i</sub></em>인 점프대를 밟으면 그 어떤 요인과도 관계없이 다음 <em>h<sub>i</sub></em>칸 위를 비행한 뒤 그다음 칸에 착지한다. 다음 예시를 확인해 보자.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0dce84cd-42a2-47f2-9052-404dc651145a/-/preview/" style="height: 149px; width: 640px;"></p>

<p>자전거를 타고 1번 칸에서 출발해 앞으로 달리면 다음과 같은 일들이 순서대로 일어난다.</p>

<ol>
	<li>1번 칸에 점프대가 없으므로 2번 칸으로 주행한다.</li>
	<li>2번 칸에 높이가 1인 점프대가 있어 3번 칸 위를 비행하여 4번 칸에 착지한다.</li>
	<li>4번 칸에 높이가 2인 점프대가 있어 5, 6번 칸 위를 비행하여 7번 칸에 착지한다.</li>
	<li>7번 칸에 점프대가 없으므로 8번 칸으로 주행한다.</li>
	<li>8번 칸에 높이가 3인 점프대가 있어 9번 칸 위를 비행하여 저 멀리 나아간다. (만일 도로가 충분히 길었다면 가상의 12번 칸에 착지하였을 것이다.)</li>
</ol>

<p>시은이는 각 칸에서 자전거를 타고 출발해 앞으로 달릴 때, 도로 위 몇 개의 칸을 밟게 될지 알아보려 한다. 하지만 <em>N</em>개의 칸에 대해 일일이 실험해 보는 건 너무 수고스럽고 귀찮은 일이 아닌가? 다음과 같은 표를 만들고 열심히 머리를 굴리던 시은이는 깨달음을 얻었다. 오른쪽에 있는 칸의 답을 활용해 왼쪽에 있는 칸의 답을 쉽게 구할 수 있다는 것이다!</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 500px;">
	<tbody>
		<tr>
			<td style="text-align: center;">출발한 칸</td>
			<td style="text-align: center;">답</td>
			<td style="text-align: center;">밟는 칸</td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;">1, 2, 4, 7, 8</td>
		</tr>
		<tr>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">2, 4, 7, 8</td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">3, 4, 7, 8</td>
		</tr>
		<tr>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">4, 7, 8</td>
		</tr>
		<tr>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">5, 7, 8</td>
		</tr>
		<tr>
			<td style="text-align: center;">6</td>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">6, 7, 8</td>
		</tr>
		<tr>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">7, 8</td>
		</tr>
		<tr>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">9</td>
		</tr>
	</tbody>
</table>

<p>점프대가 없는 1번 칸의 답은 바로 다음 2번 칸의 답에 1을 더한 것과 같다. 높이 1의 점프대가 있는 2번 칸의 답은 한 칸을 건너뛴 4번 칸의 답에 1을 더한 것과 같다. 다른 칸들도 같은 방식으로 답을 구할 수 있다. 특히 도로를 벗어나게 되는 8번 칸과 9번 칸의 답은 1(각각 밟는 칸이 8번, 9번뿐이다) 임을 확인하자.</p>

<p>여러분이 할 일은 이 놀라운 사실을 이용해 시은이의 궁금증을 해결하는 프로그램을 만드는 것이다. 이 사실을 이용하지 않으면 채점 결과로 시간초과를 받을 수 있으니 되도록이면 이용해 보자.</p>

### 입력 

 <p>첫번째 줄에 도로의 길이 <em>N</em>이 주어진다.</p>

<p>두번째 줄에 1번 칸부터 <em>N</em>번 칸까지 순서대로 각 칸에 설치된 점프대의 높이가 공백을 구분으로 주어진다. 단, 점프대가 없는 칸은 0이 주어진다.</p>

### 출력 

 <p>1번 칸부터 <em>N</em>번 칸까지 순서대로, 각 칸에서 자전거를 타고 앞으로 달리면 총 몇 개의 칸을 밟게 되는지 출력한다. 각 출력은 공백으로 구분한다.</p>

