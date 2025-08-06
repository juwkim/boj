# [Silver I] Treadmill - 4639 

[문제 링크](https://www.acmicpc.net/problem/4639) 

### 성능 요약

메모리: 110908 KB, 시간: 116 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 8월 7일 02:04:12

### 문제 설명

<p>The You'reFat treadmill company has decided to enhance its treadmills to allow users to run workout programs from an audio program (either online streaming audio or from a CD). The program will have upbeat music and encouragement from an instructor. Chirps can be inserted into the audio program to indicate changes in speed and inclination. For example, when it is time to increase the treadmill speed, the music will temporarily stop while the treadmill gets the new speed from the chirp, and then the music resumes. The treadmill can handle speeds from 0 to 7 miles per hour, and inclinations of 0 to 7 degrees.</p>

<p>A program consists of a sequence of samples. Each sample will range from 0 (minimum value) to 9 (maximum value). There will be three samples per second. Each chirp consists of a sequence of bits. A 0 bit consists of two samples of either 4 or 5. A 1 bit consists of two samples, the first being either 0 or 1, and the second one being either 8 or 9. The chirp starts with the bits "01". The next three bits represent the new speed (least significant bit first). This is followed by three bits for the new inclination (also least significant bit first). Note that every chirp includes both speed and inclination, even if one or the other doesn't change. A chirp representing a speed of 3 miles per hour, and an inclination of 6 degrees would look like:</p>

<table class="table table-bordered" style="width:60%">
	<tbody>
		<tr>
			<td>Samples</td>
			<td>5</td>
			<td>5</td>
			<td>1</td>
			<td>9</td>
			<td>1</td>
			<td>9</td>
			<td>1</td>
			<td>9</td>
			<td>4</td>
			<td>5</td>
			<td>5</td>
			<td>4</td>
			<td>0</td>
			<td>9</td>
			<td>1</td>
			<td>8</td>
		</tr>
		<tr>
			<td>Bits</td>
			<td colspan="2">0</td>
			<td colspan="2">1</td>
			<td colspan="2">1</td>
			<td colspan="2">1</td>
			<td colspan="2">0</td>
			<td colspan="2">0</td>
			<td colspan="2">1</td>
			<td colspan="2">1</td>
		</tr>
		<tr>
			<td>Meaning</td>
			<td colspan="4">Start bits</td>
			<td colspan="6">Speed: 3 mph</td>
			<td colspan="6">Inclination: 6 degrees</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>The input file consists of one or more programs. Each program is implicitly numbered starting at 1. The first line contains a single integer n, which is the number of programs that follow. Each program is a sequence of samples. Each line of a program will contain exactly 30 samples, except the last line, which may contain fewer. The end of each program will be represented by a sample with the value 10.</p>

<p>Note that:</p>

<ul>
	<li>Any value from 0 to 9 may be a sample in the background music, but the starting bit sequence for a chirp "01" (middle, middle, low, high) will not occur in the background music.</li>
	<li>Chirps consume time.</li>
	<li>Each workout is less than 60 minutes long.</li>
	<li>A chirp with speed 0 does not imply the end of the workout.</li>
	<li>A chirp may be preceded by one or more samples with the value 4 or 5.</li>
	<li>Chirps do not necessarily begin on an even second boundary.</li>
	<li>Each chirp is well-formed (only proper 0 or 1 bits will occur)</li>
</ul>

### 출력 

 <p>For each audio program, you should first print a line "Program n" where n is the program number. Then, you should print the time, speed and inclination of each chirp in that audio program. Each chirp should produce one line of output in the form "mm:ss Speed S Inclination I". Both minutes and seconds should be printed with a leading zero ("00" to "59"). The time of a chirp is the time for the first sample of the start bits, ignoring any fractional seconds. Both speed S and inclination I should be printed as single decimal digits. There should be a single space between each item in the output.</p>

