# [Bronze I] 이름궁합 테스트 - 17269 

[문제 링크](https://www.acmicpc.net/problem/17269) 

### 성능 요약

메모리: 29200 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>시윤이는 좋아하는 이성이 생기면 가장 먼저 이름궁합부터 본다. 이름궁합을 보는 방법은 간단하다. 먼저 이름을 알파벳 대문자로 적는다. 각 알파벳 대문자에는 다음과 같이 알파벳을 적는데 필요한 획수가 주어진다. 예를 들어, 두 사람의 이름인 LEESIYUN, MIYAWAKISAKURA 를 같이 표현했을 때 다음과 같이 먼저 주어진 이름부터 한 글자씩 적는다.</p>

<table class="table table-bordered">
	<thead>
		<tr>
			<th>알파벳</th>
			<th>A</th>
			<th>B</th>
			<th>C</th>
			<th>D</th>
			<th>E</th>
			<th>F</th>
			<th>G</th>
			<th>H</th>
			<th>I</th>
			<th>J</th>
			<th>K</th>
			<th>L</th>
			<th>M</th>
			<th>N</th>
			<th>O</th>
			<th>P</th>
			<th>Q</th>
			<th>R</th>
			<th>S</th>
			<th>T</th>
			<th>U</th>
			<th>V</th>
			<th>W</th>
			<th>X</th>
			<th>Y</th>
			<th>Z</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>획수</th>
			<td>3</td>
			<td>2</td>
			<td>1</td>
			<td>2</td>
			<td>4</td>
			<td>3</td>
			<td>1</td>
			<td>3</td>
			<td>1</td>
			<td>1</td>
			<td>3</td>
			<td>1</td>
			<td>3</td>
			<td>2</td>
			<td>1</td>
			<td>2</td>
			<td>2</td>
			<td>2</td>
			<td>1</td>
			<td>2</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>2</td>
			<td>2</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>두 사람의 이름을 알파벳 대문자로 표현한 뒤, 한 글자씩 번갈아가며 적는다.</p>

<p>예시 :  L M E I E Y S A I W Y A U K N I <strong>S A K U R A</strong></p>

<p>예시처럼 <strong>이름이 남을 경우엔 뒤에 남은 글자인 S A K U R A를 맨 뒤에 적는다.</strong> 그러고 나서 알파벳을 대응하는 숫자로 바꾸고 각 숫자와 그 숫자의 오른쪽 숫자와 더한 것을 밑에 적는다. 더한 숫자가 10이 넘을 경우엔 일의 자리 수만 남긴다. 이 과정을 반복하여 숫자가 2개만 남았을 때 남은 숫자가 두 사람의 궁합이 좋을 확률이 된다.</p>

<p>과정을 자세히 나타내면 다음과 같다.</p>

<pre>초기 상태 : 1 3 4 1 4 2 1 3 1 1 2 3 1 3 2 1 1 3 3 1 2 3
한번 수행 :  4 7 5 5 6 3 4 4 2 3 5 4 4 5 3 2 4 6 4 3 5
두번 수행 :   1 2 0 1 9 7 8 6 5 8 9 8 9 8 5 6 0 0 7 8
세번 수행 :    3 2 1 0 6 5 4 1 3 7 7 7 7 3 1 6 0 7 5
...
19번 수행 :                  5 7 0
20번 수행 :                   2 7
</pre>

<p>따라서 LEESIYUN와 MIYAWAKISAKURA이 궁합이 좋을 확률이 27%이다.</p>

### 입력 

 <p>첫 번째 줄에 이름의 길이 <em>N</em>과 <em>M</em>을 받는다. (2 ≤ <em>N</em>, <em>M</em> ≤ 100)</p>

<p>다음 줄에 이름 <em>A</em>와 <em>B</em>를 입력받는다. 이름은 반드시 알파벳 대문자만 주어진다.</p>

### 출력 

 <p><em>A</em>와 <em>B</em>의 이름궁합이 좋을 확률을 %로 출력한다. 단, 십의 자리가 0일 경우엔 일의 자리만 출력한다.</p>

