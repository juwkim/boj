# [Silver V] Brainman - 7554 

[문제 링크](https://www.acmicpc.net/problem/7554) 

### 성능 요약

메모리: 115004 KB, 시간: 228 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>Raymond Babbitt drives his brother Charlie mad. Recently Raymond counted 246 toothpicks spilled all over the floor in an instant just by glancing at them. And he can even count Poker cards. Charlie would love to be able to do cool things like that, too. He wants to beat his brother in a similar task.</p>

<p>Here’s what Charlie thinks of. Imagine you get a sequence of N numbers. The goal is to move the numbers around so that at the end the sequence is ordered. The only operation allowed is to swap two adjacent numbers. Let us try an example:</p>

<p>So the sequence (2 8 0 3) can be sorted with nine swaps of adjacent numbers. However, it is even possible to sort it with three such swaps:</p>

<p> </p>

<table class="table" style="width:40%">
	<tbody>
		<tr>
			<th>Start with:</th>
			<td>2</td>
			<td>8</td>
			<td>0</td>
			<td>3</td>
		</tr>
		<tr>
			<th>swap (2 8)</th>
			<td>8</td>
			<td>2</td>
			<td>0</td>
			<td>3</td>
		</tr>
		<tr>
			<th>swap (2 0)</th>
			<td>8</td>
			<td>0</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<th>swap (2 3)</th>
			<td>8</td>
			<td>0</td>
			<td>3</td>
			<td>2</td>
		</tr>
		<tr>
			<th>swap (8 0)</th>
			<td>0</td>
			<td>8</td>
			<td>3</td>
			<td>2</td>
		</tr>
		<tr>
			<th>swap (8 3)</th>
			<td>0</td>
			<td>3</td>
			<td>8</td>
			<td>2</td>
		</tr>
		<tr>
			<th>swap (8 2)</th>
			<td>0</td>
			<td>3</td>
			<td>2</td>
			<td>8</td>
		</tr>
		<tr>
			<th>swap (3 2)</th>
			<td>0</td>
			<td>2</td>
			<td>3</td>
			<td>8</td>
		</tr>
		<tr>
			<th>swap (3 8)</th>
			<td>0</td>
			<td>2</td>
			<td>8</td>
			<td>3</td>
		</tr>
		<tr>
			<th>swap (8 3)</th>
			<td>0</td>
			<td>2</td>
			<td>3</td>
			<td>8</td>
		</tr>
	</tbody>
</table>

<p>The question is: What is the minimum number of swaps of adjacent numbers to sort a given sequence? Since Charlie does not have Raymond’s mental capabilities, he decides to cheat. Here is where you come into play. He asks you to write a computer program for him that answers the question. Rest assured he will pay a very good prize for it.</p>

<p> </p>

<table class="table" style="width:40%">
	<tbody>
		<tr>
			<th>Start with:</th>
			<td>2</td>
			<td>8</td>
			<td>0</td>
			<td>3</td>
		</tr>
		<tr>
			<th>swap (8 0)</th>
			<td>2</td>
			<td>0</td>
			<td>8</td>
			<td>3</td>
		</tr>
		<tr>
			<th>swap (2 0)</th>
			<td>0</td>
			<td>2</td>
			<td>8</td>
			<td>3</td>
		</tr>
		<tr>
			<th>swap (8 3)</th>
			<td>0</td>
			<td>2</td>
			<td>3</td>
			<td>8</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>The first line contains the number of scenarios.</p>

<p>For every scenario, you are given a line containing first the length N (1 ≤ N ≤ 1000) of the sequence, followed by the N elements of the sequence (each element is an integer in [−1000000, 1000000]). All numbers in this line are separated by single blanks.</p>

### 출력 

 <p>Start the output for every scenario with a line containing “Scenario #i:”, where i is the number of the scenario starting at 1. Then print a single line containing the minimal number of swaps of adjacent numbers that are necessary to sort the given sequence. Terminate the output for the scenario with a blank line.</p>

