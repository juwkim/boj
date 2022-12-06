# [Silver V] 매직스퀘어 - 15739 

[문제 링크](https://www.acmicpc.net/problem/15739) 

### 성능 요약

메모리: 31352 KB, 시간: 76 ms

### 분류

구현(implementation)

### 문제 설명

<p>수학에서 행렬(行列, matrix)은 수나 기호, 수식 등을 네모꼴로 배열한 것으로, 가로줄을 행(row), 세로줄을 열(column)이라고 한다. 특히 행과 열의 개수가 같은 행렬을 정방행렬(square matrix)이라고 한다.</p>

<p>매직스퀘어(magic square,마방진,魔方陣)는 다음 2 가지 성질을 만족하는 정방행렬이다.</p>

<ol>
	<li>행렬의 원소는 1부터 `n*n`(n의 제곱) 범위의 정수로 구성하며, 중복되는 수가 없이 모두 달라야 한다.</li>
	<li>행의 합, 열의 합, 2개의 대각선의 수열의 합은 모두 같으며, 합은 다음 식으로 구한다. </li>
</ol>

<p style="text-align: center;">n × (n<sup>2</sup> + 1) / 2</p>

<p>즉, n=2 이면 합은 5 이고, n=3이면 합은 15 이고, n=4이면, 합은 34 이다.</p>

<p>예를 들어, 다음은 매직스퀘어의 예이다. (n=2 인 매직스퀘어는 없다.)</p>

<table class="table" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 33%;">
			<pre style="text-align: center;">2 7 6
9 5 1
4 3 8</pre>
			</td>
			<td style="width: 34%;">
			<pre style="text-align: center;">4 14 15 1
9 7 6 12
5 11 10 8
16 2 3 13</pre>
			</td>
			<td style="width: 33%;">
			<pre style="text-align: center;">11 24 7 20 3
4 12 25 8 16
17 5 13 21 9
10 18 1 14 22
23 6 19 2 15</pre>
			</td>
		</tr>
	</tbody>
</table>

<p>정수 리스트의 리스트(또는 정수 배열의 배열)로 표현한 임의의 정방행렬을 받아서, 매직스퀘어인지 확인하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N(3 ≤  N ≤ 100)가 주어지고 둘째 줄부터 N개의 줄에 걸쳐 N개의 숫자가 주어진다. N개의 수의 범위는 1이상 n<sup>2</sup>이하 이다.</p>

### 출력 

 <p>입력된 N개의 숫자가 나타내는 정방행렬이 매직스퀘어라면 TRUE, 아니라면 FALSE를 출력한다.</p>

