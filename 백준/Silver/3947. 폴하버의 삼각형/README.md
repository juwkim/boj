# [Silver II] 폴하버의 삼각형 - 3947 

[문제 링크](https://www.acmicpc.net/problem/3947) 

### 성능 요약

메모리: 160676 KB, 시간: 644 ms

### 분류

조합론, 다이나믹 프로그래밍, 수학

### 제출 일자

2025년 2월 8일 02:39:37

### 문제 설명

<p>1부터 n까지 m제곱의 합은 다음과 같다.</p>

<pre>S(n,m) = SUM (j = i to n) (j<sup>m</sup>)</pre>

<p>이 식은 n의 차수가 m+1인 다항식으로 나타낼 수 있다.</p>

<pre>S(n,m) = SUM (k = 1 to m+1) (F(m,k) * n<sup>k</sup>)</pre>

<p>예를 들면 다음과 같다.</p>

<pre>S(n,1) = (1 + ... + n) = (1/2)*n<sup>2</sup> + (1/2)*n
S(n,2) = (1 + ... + n<sup>2</sup>) = (1/3)*n<sup>3</sup> + (1/2)*n<sup>2</sup> + (1/6)*n
S(n,3) = (1 + ... + n<sup>3</sup>) = (1/4)*n<sup>4</sup> + (1/2)*n<sup>3</sup> + (1/4)*n<sup>2</sup>
S(n,4) = (1 + ... + n<sup>4</sup>) = (1/5)*n<sup>5</sup> + (1/2)*n<sup>4</sup> + (1/3)*n<sup>3</sup> - (1/30)*n</pre>

<p>위의 식에 나오는 계수 F(m,k)는 폴하버의 삼각형을 이룬다.</p>

<table class="table table-bordered" style="width:49%">
	<tbody>
		<tr>
			<td style="width:7%">1</td>
			<td style="width:7%"> </td>
			<td style="width:7%"> </td>
			<td style="width:7%"> </td>
			<td style="width:7%"> </td>
			<td style="width:7%"> </td>
			<td style="width:7%"> </td>
		</tr>
		<tr>
			<td>1/2</td>
			<td>1/2</td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td>1/6</td>
			<td>1/2</td>
			<td>1/3</td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td>0</td>
			<td>1/4</td>
			<td>1/2</td>
			<td>1/4</td>
			<td> </td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td>-1/30</td>
			<td>0</td>
			<td>1/3</td>
			<td>1/2</td>
			<td>1/5</td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td>0</td>
			<td>-1/12</td>
			<td>0</td>
			<td>5/12</td>
			<td>1/2</td>
			<td>1/6</td>
			<td> </td>
		</tr>
		<tr>
			<td>1/42</td>
			<td>0</td>
			<td>-1/6</td>
			<td>0</td>
			<td>1/2</td>
			<td>1/2</td>
			<td>1/7</td>
		</tr>
	</tbody>
</table>

<p>F(m,k)에서 m은 행이고, 위에서부터 0번이다. k는 열이고, 왼쪽에서부터 1번이다.</p>

<p>폴하버의 삼각형은 아래와 같이 구할 수 있다.</p>

<ol>
	<li>j>1인 F(i,j) = (i/j)*F(i-1,j-1)</li>
	<li>i번째 row의 수를 다 더했을 때 1이 되도록 F(i,1) 을 정해야 한다</li>
</ol>

<p>m,k 가 주어졌을 때, F(m,k)를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 P (1 ≤ P ≤ 1000)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, m과 k가 공백으로 구분되어져 있다. (0 ≤ m ≤ 400, 1 ≤ k ≤ n+1)</p>

### 출력 

 <p>각 테스트 케이스에 대해서, F(m,k)를 출력한다. 만약 결과가 정수라면 정수로 출력하고, 정수가 아니라면, 기약분수로 출력한다.</p>

