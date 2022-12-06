# [Silver IV] VCR++ Codes - 20382 

[문제 링크](https://www.acmicpc.net/problem/20382) 

### 성능 요약

메모리: 123980 KB, 시간: 368 ms

### 분류

비트마스킹(bitmask), 구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p>VCR plus codes were designed to make programming VCRs an easier task. A VCR plus code is a single number, usually about 5 or 6 digits, which encapsulates channel, date, start time, and program length information. A similar code is the VCR++ code, which fits entirely within a 32-bit integer. The VCR++ code is structed as shown in the table below (0 is the low-order bit).</p>

<table class="table table-bordered table-center-30">
	<thead>
		<tr>
			<th>Offset</th>
			<th>Bits</th>
			<th>Field</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>4</td>
			<td>Program length</td>
		</tr>
		<tr>
			<td>4</td>
			<td>6</td>
			<td>Start time</td>
		</tr>
		<tr>
			<td>10</td>
			<td>5</td>
			<td>Day of month</td>
		</tr>
		<tr>
			<td>15</td>
			<td>4</td>
			<td>Month</td>
		</tr>
		<tr>
			<td>19</td>
			<td>6</td>
			<td>Channel</td>
		</tr>
		<tr>
			<td>25</td>
			<td>7</td>
			<td>Year</td>
		</tr>
	</tbody>
</table>

<p>The program length and start time fields are in increments of 30 minutes. In the start time field, 0 represents midnight, 1 represents 12:30 AM, 2 represents 1:00 AM, and so on, up to 47 which represents 11:30 PM. The year field is added to 1994 to determine the actual year. For example, if the year field contains 3, then the year represented is 1994 + 3 = 1997. The day of month field ranges from 1 to 31, the month field from 1 to 12 (representing January through December, respectively), and the channel field from 1 to 63.</p>

<p>For example, a one-hour program on channel 28 starting at 10:00 AM on July 30, 1994, would have the VCR++ code of 14940482. This is the decimal representation of the binary number 111000111111100101000010, generated from the above information as shown below.</p>

<pre>0000000  011100  0111  11110  010100  0010
 Year    Channel Month  Day   Start   Length
</pre>

### 입력 

 <p>Each line of the input for this problem specifies programming information for which a VCR++ code is to be output. The end of the input is marked by the end of the file.</p>

<p>Each input line is formatted as follows. The keyword "Channel" always begins in column 1, followed by a space, the channel number, a comma, and another space. Next, the name of the month is spelled out (with only the first letter capitalized), followed by a space, the day of the month, another space, the year, a comma, and another space. The start time is specified next, with the hour and minutes separated by a colon. Next come either the characters "am" or "pm", a space, the length of the program in minutes, and then the characters "min". Note that the staring time will always fall on a half-hour boundary, and the program length will always be a multiple of 30 minutes.</p>

### 출력 

 Empty

