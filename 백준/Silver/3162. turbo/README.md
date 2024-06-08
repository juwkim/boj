# [Silver III] turbo - 3162 

[문제 링크](https://www.acmicpc.net/problem/3162) 

### 성능 요약

메모리: 110992 KB, 시간: 136 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 6월 9일 02:59:14

### 문제 설명

<p>A new TV set, besides the regular capability to directly select a channel with the remote control, is equipped with the new "turbo" mode with an associated key (labeled with the letter T) on the remote control. </p>

<p>Turbo mode makes it easier to cycle through a number of previously selected channels. For usual operation, the user selects a channel by pressing the appropriate key on the remote control. </p>

<p>Let the currently displayed channel be channel X. </p>

<p>After pressing the T key, the TV set enters the turbo mode, and changes to the first channel displayed after the last change to channel X. Additional presses of the T key make the TV set cycle through channels that were displayed between the two appearances of the channel X, channel X included. In one cycle, the TV set displays each channel only once, in order of their first appearance. </p>

<p>If the first appearance of the channel X is just before entering the turbo mode, the cycle starts with the first selected channel. </p>

<p>The TV set leaves the turbo mode when the user manually selects a channel. </p>

<p>For example, if the pressed keys are 1, 2, 3, T, T, T, T, T, 2, 4, 1, T, T, T and T: </p>

<table class="table table-bordered">
	<thead>
		<tr>
			<th>Step</th>
			<th>Pressed key</th>
			<th>Explanation</th>
			<th>Channel displayed</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1.</td>
			<td>1</td>
			<td>Manual select</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2.</td>
			<td>2</td>
			<td>Manual select</td>
			<td>2</td>
		</tr>
		<tr>
			<td>3.</td>
			<td>3</td>
			<td>Manual select</td>
			<td>3</td>
		</tr>
		<tr>
			<td>4.</td>
			<td>T</td>
			<td>When the TV enters turbo mode, the displayed channel is 3 (first appearance). The turbo cycle starts from the first selected channel (1 in this case)</td>
			<td>1</td>
		</tr>
		<tr>
			<td>5.</td>
			<td>T</td>
			<td>After channel 1, channel 2 was selected</td>
			<td>2</td>
		</tr>
		<tr>
			<td>6.</td>
			<td>T</td>
			<td>After channel 2, channel 3 was selected</td>
			<td>3</td>
		</tr>
		<tr>
			<td>7.</td>
			<td>T</td>
			<td>The cycle started in step 4 is repeated</td>
			<td>1</td>
		</tr>
		<tr>
			<td>8.</td>
			<td>T</td>
			<td>After channel 1, channel 2 was selected</td>
			<td>2</td>
		</tr>
		<tr>
			<td>9.</td>
			<td>2</td>
			<td>Manual select, the TV set leaves turbo mode</td>
			<td>2</td>
		</tr>
		<tr>
			<td>10.</td>
			<td>4</td>
			<td>Manual select</td>
			<td>4</td>
		</tr>
		<tr>
			<td>11.</td>
			<td>1</td>
			<td>Manual select</td>
			<td>1</td>
		</tr>
		<tr>
			<td>12.</td>
			<td>T</td>
			<td>The last occurrence of channel 1 was in step 7, the TV set changes to the next displayed channel</td>
			<td>2</td>
		</tr>
		<tr>
			<td>13.</td>
			<td>T</td>
			<td>If we would display channel 2 from step 9, it will be its second appearance, so we skip it</td>
			<td>4</td>
		</tr>
		<tr>
			<td>14.</td>
			<td>T</td>
			<td>The channel X is also included in the cycle</td>
			<td>1</td>
		</tr>
		<tr>
			<td>15.</td>
			<td>T</td>
			<td>The cycle started in step 12 is repeated</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

<p>Write a program that, given the sequence of pressed keys, determines which channel is displayed each time the T key is pressed. </p>

<p>The TV set has 99 channels labeled with numbers from 1 to 99 and the first pressed key will not be T. </p>

### 입력 

 <p>The first line of input contains an integer N, 1 ≤ N ≤ 10 000. </p>

<p>Each of the following N lines contains a number or the letter T. </p>

### 출력 

 <p>For each time the T key is pressed, output the channel that is displayed. </p>

