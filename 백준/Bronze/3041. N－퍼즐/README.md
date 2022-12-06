# [Bronze I] N-퍼즐 - 3041 

[문제 링크](https://www.acmicpc.net/problem/3041) 

### 성능 요약

메모리: 29200 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>N-퍼즐은 많은 다양한 형태와 이름이 있다. 이번 문제에서 우리가 살펴볼 것은 15-퍼즐이다.</p>

<p>15-퍼즐은 4*4보드에서 움직일 수 있는 정사각형으로 이루어져 있고, 한 정사각형은 빠져있다. 정사각형은 A부터 O까지 이름이 붙여져 있다. 이 퍼즐을 풀면 다음과 같은 그림이 된다.</p>

<table class="table table-bordered" style="width:100px">
	<tbody>
		<tr>
			<td>A</td>
			<td>B</td>
			<td>C</td>
			<td>D</td>
		</tr>
		<tr>
			<td>E</td>
			<td>F</td>
			<td>G</td>
			<td>H</td>
		</tr>
		<tr>
			<td>I</td>
			<td>J</td>
			<td>K</td>
			<td>L</td>
		</tr>
		<tr>
			<td>M</td>
			<td>N</td>
			<td>O</td>
			<td>.</td>
		</tr>
	</tbody>
</table>

<p>우리는 이러한 15-퍼즐에서 흩어짐 정도를 계산할 수 있다. 흩어짐 정도는 각 정사각형의 현재 위치와 퍼즐을 풀었을 때의 위치와의 거리의 합이다.</p>

<p>두 정사각형의 거리는 그 두 정사각형 사이의 맨해튼 거리이다.</p>

<p>15-퍼즐이 주어졌을 때, 흩어짐 정도를 계산하는 프로그램을 작성하시오.</p>

### 입력 

 <p>4줄에 걸쳐 현재 퍼즐의 상태가 주어진다.</p>

### 출력 

 <p>퍼즐의 흩어짐 정도를 출력한다.</p>

