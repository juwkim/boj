# [Bronze I] 문자열 압축 해제 - 23746 

[문제 링크](https://www.acmicpc.net/problem/23746) 

### 성능 요약

메모리: 115068 KB, 시간: 112 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>특정 소문자 문자열 패턴을 대문자 한 글자로 압축하는 프로그램 SPC(String Pattern Compressor)가 있다.</p>

<p>예를 들어, 다음과 같은 방법으로 압축하는 경우, “$\text{aabbaaac}$”는 “$\text{ABAC}$”로 압축된다.</p>

<table class="table table-bordered table-center-30">
	<tbody>
		<tr>
			<td style="text-align: center;">소문자 문자열 패턴</td>
			<td style="text-align: center;">대문자</td>
		</tr>
		<tr>
			<td style="text-align: center;">$\text{aa}$</td>
			<td style="text-align: center;">$\text{A}$</td>
		</tr>
		<tr>
			<td style="text-align: center;">$\text{bba}$</td>
			<td style="text-align: center;">$\text{B}$</td>
		</tr>
		<tr>
			<td style="text-align: center;">$\text{c}$</td>
			<td style="text-align: center;">$\text{C}$</td>
		</tr>
	</tbody>
</table>

<p>압축 프로그램과 압축된 문자열이 주어지면, 압축되기 전 문자열의 일부를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 압축 방법의 개수 $N$이 주어진다. ($1 \le N \le 26$)</p>

<p>두 번째 줄부터 $N$개의 줄에 소문자 문자열 패턴과 대응되는 대문자가 공백으로 구분되어 주어진다. 각 소문자 문자열 패턴의 길이는 $1\,000$을 넘지 않으며, 같은 대문자는 두 번 이상 주어지지 않는다.</p>

<p>$N+1$번째 줄에 압축된 문자열이 주어진다. 압축된 문자열 길이는 $1\,000$을 넘지 않는다.</p>

<p>마지막 줄에 두 정수 $S$와 $E$가 주어진다. ($1 \le S \le E \le $ (압축되기 전 문자열 길이))</p>

### 출력 

 <p>압축되기 전 문자열의 $S$번째 문자에서 $E$번째 문자까지 출력한다.</p>

