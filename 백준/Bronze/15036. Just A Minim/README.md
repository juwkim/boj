# [Bronze III] Just A Minim - 15036 

[문제 링크](https://www.acmicpc.net/problem/15036) 

### 성능 요약

메모리: 122244 KB, 시간: 108 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Listening to music is a good way to take one’s mind off the monotony of typing out solution after correct solution.</p>

<p>However, it can be very annoying to start listening to a tune and then for time to run out early, cutting the listening short. How much more satisfying it would be if you could choose tunes to fit the time available!</p>

<p>With this in mind, you have found a way to code musical scores into simple lists of numbers representing the length of the notes in each tune as follows:</p>

<table class="table table-bordered" style="width:30%">
	<thead>
		<tr>
			<th>Code</th>
			<th>Name</th>
			<th>Length</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>breve</td>
			<td>2 notes</td>
		</tr>
		<tr>
			<td>1</td>
			<td>semibreve</td>
			<td>1 notes</td>
		</tr>
		<tr>
			<td>2</td>
			<td>minim</td>
			<td>1/2 notes</td>
		</tr>
		<tr>
			<td>4</td>
			<td>crotchet</td>
			<td>1/4 notes</td>
		</tr>
		<tr>
			<td>8</td>
			<td>quaver</td>
			<td>1/8 notes</td>
		</tr>
		<tr>
			<td>16</td>
			<td>semiquaver</td>
			<td>1/16 notes</td>
		</tr>
	</tbody>
</table>

<p>Given such a list of numbers, calculate the length of the tune in notes.</p>

### 입력 

 <ul>
	<li>One line containing the integer N (1 ≤ N ≤ 2000), the number of values in the tune.</li>
	<li>one line containing N integers each representing the length of a value using the codes above.</li>
</ul>

### 출력 

 <p>Output the length of the tune, as a real number of notes. The output must be accurate to an absolute or relative error of at most 10<sup>−6</sup>.</p>

