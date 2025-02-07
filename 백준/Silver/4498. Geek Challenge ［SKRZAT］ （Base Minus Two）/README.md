# [Silver II] Geek Challenge [SKRZAT] (Base Minus Two) - 4498 

[문제 링크](https://www.acmicpc.net/problem/4498) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 정수론

### 제출 일자

2025년 2월 7일 16:36:25

### 문제 설명

<p>Geek Challenge [SKRZAT] is an old, old game from Poland that uses a game console with two buttons plus a joy stick. As is true to its name, the game communicates in binary, so that one button represents a zero and the other a one. Even more true to its name, the game chooses to communicate so that the base of the number system is minus two, not plus two, so we’ll call this representation “Weird Binary”. Thus the bit positions label the powers of minus two, as seen in the following five-bit tables:</p>

<table class="table table-bordered" style="width:500px">
	<tbody>
		<tr>
			<td style="text-align: center;"><strong>Bits</strong></td>
			<td style="text-align: center;"><strong>Value</strong></td>
			<td style="text-align: center;"><strong>Bits</strong></td>
			<td style="text-align: center;"><strong>Value</strong></td>
			<td style="text-align: center;"><strong>Bits</strong></td>
			<td style="text-align: center;"><strong>Value</strong></td>
			<td style="text-align: center;"><strong>Bits</strong></td>
			<td style="text-align: center;"><strong>Value</strong></td>
		</tr>
		<tr>
			<td style="text-align: center;">00000</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">01000</td>
			<td style="text-align: center;">-8</td>
			<td style="text-align: center;">10000</td>
			<td style="text-align: center;">16</td>
			<td style="text-align: center;">11000</td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;">00001</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">01001</td>
			<td style="text-align: center;">-7</td>
			<td style="text-align: center;">10001</td>
			<td style="text-align: center;">17</td>
			<td style="text-align: center;">11001</td>
			<td style="text-align: center;">9</td>
		</tr>
		<tr>
			<td style="text-align: center;">00010</td>
			<td style="text-align: center;">-2</td>
			<td style="text-align: center;">01010</td>
			<td style="text-align: center;">-10</td>
			<td style="text-align: center;">10010</td>
			<td style="text-align: center;">14</td>
			<td style="text-align: center;">11010</td>
			<td style="text-align: center;">6</td>
		</tr>
		<tr>
			<td style="text-align: center;">00011</td>
			<td style="text-align: center;">-1</td>
			<td style="text-align: center;">01011</td>
			<td style="text-align: center;">-9</td>
			<td style="text-align: center;">10011</td>
			<td style="text-align: center;">15</td>
			<td style="text-align: center;">11011</td>
			<td style="text-align: center;">7</td>
		</tr>
		<tr>
			<td style="text-align: center;">00100</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">01100</td>
			<td style="text-align: center;">-4</td>
			<td style="text-align: center;">10100</td>
			<td style="text-align: center;">20</td>
			<td style="text-align: center;">11100</td>
			<td style="text-align: center;">12</td>
		</tr>
		<tr>
			<td style="text-align: center;">00101</td>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;">01101</td>
			<td style="text-align: center;">-3</td>
			<td style="text-align: center;">10101</td>
			<td style="text-align: center;">21</td>
			<td style="text-align: center;">11101</td>
			<td style="text-align: center;">13</td>
		</tr>
		<tr>
			<td style="text-align: center;">00110</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">01110</td>
			<td style="text-align: center;">-6</td>
			<td style="text-align: center;">10110</td>
			<td style="text-align: center;">18</td>
			<td style="text-align: center;">11110</td>
			<td style="text-align: center;">10</td>
		</tr>
		<tr>
			<td style="text-align: center;">00111</td>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">01111</td>
			<td style="text-align: center;">-5</td>
			<td style="text-align: center;">10111</td>
			<td style="text-align: center;">19</td>
			<td style="text-align: center;">11111</td>
			<td style="text-align: center;">11</td>
		</tr>
	</tbody>
</table>

<p> </p>

<table class="table table-bordered" style="width:500px">
	<tbody>
		<tr>
			<td style="text-align: center;"><strong>Bits</strong></td>
			<td style="text-align: center;"><strong>Value</strong></td>
			<td style="text-align: center;"><strong>Bits</strong></td>
			<td style="text-align: center;"><strong>Value</strong></td>
			<td style="text-align: center;"><strong>Bits</strong></td>
			<td style="text-align: center;"><strong>Value</strong></td>
			<td style="text-align: center;"><strong>Bits</strong></td>
			<td style="text-align: center;"><strong>Value</strong></td>
		</tr>
		<tr>
			<td style="text-align: center;">01010</td>
			<td style="text-align: center;">-10</td>
			<td style="text-align: center;">00010</td>
			<td style="text-align: center;">-2</td>
			<td style="text-align: center;">11010</td>
			<td style="text-align: center;">6</td>
			<td style="text-align: center;">10010</td>
			<td style="text-align: center;">14</td>
		</tr>
		<tr>
			<td style="text-align: center;">01011</td>
			<td style="text-align: center;">-9</td>
			<td style="text-align: center;">00011</td>
			<td style="text-align: center;">-1</td>
			<td style="text-align: center;">11011</td>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;">10011</td>
			<td style="text-align: center;">15</td>
		</tr>
		<tr>
			<td style="text-align: center;">01000</td>
			<td style="text-align: center;">-8</td>
			<td style="text-align: center;">00000</td>
			<td style="text-align: center;">0</td>
			<td style="text-align: center;">11000</td>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;">10000</td>
			<td style="text-align: center;">16</td>
		</tr>
		<tr>
			<td style="text-align: center;">01001</td>
			<td style="text-align: center;">-7</td>
			<td style="text-align: center;">00001</td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">11001</td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;">10001</td>
			<td style="text-align: center;">17</td>
		</tr>
		<tr>
			<td style="text-align: center;">01110</td>
			<td style="text-align: center;">-6</td>
			<td style="text-align: center;">00110</td>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">11110</td>
			<td style="text-align: center;">10</td>
			<td style="text-align: center;">10110</td>
			<td style="text-align: center;">18</td>
		</tr>
		<tr>
			<td style="text-align: center;">01111</td>
			<td style="text-align: center;">-5</td>
			<td style="text-align: center;">00111</td>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">11111</td>
			<td style="text-align: center;">11</td>
			<td style="text-align: center;">10111</td>
			<td style="text-align: center;">19</td>
		</tr>
		<tr>
			<td style="text-align: center;">01100</td>
			<td style="text-align: center;">-4</td>
			<td style="text-align: center;">00100</td>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">11100</td>
			<td style="text-align: center;">12</td>
			<td style="text-align: center;">10100</td>
			<td style="text-align: center;">20</td>
		</tr>
		<tr>
			<td style="text-align: center;">01101</td>
			<td style="text-align: center;">-3</td>
			<td style="text-align: center;">00101</td>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;">11101</td>
			<td style="text-align: center;">13</td>
			<td style="text-align: center;">10101</td>
			<td style="text-align: center;">21</td>
		</tr>
	</tbody>
</table>

<p>Numbers are presented on the screen in Weird Binary, and then numbers are accepted in response from the console as a stream of zeroes and ones, terminated by a five-second pause.</p>

<p>You are writing a computer program to support the novice geek in playing the game by translating numbers between decimal and Weird Binary.</p>

### 입력 

 <p>The first line in the file gives the number of problems being posed without any white space. Following are that many lines. Each line will either be a conversion into Weird Binary or out of Weird Binary: the letter "b" indicates that the rest of the line is written in Weird Binary and needs to be converted to decimal; the letter "d" indicates that the rest of the line is written in decimal and needs to be converted to Weird Binary.</p>

<p>The input data are in the range to fit within a 15-bit Weird Binary number, which represents the decimal number range –10922 to 21845, inclusive.</p>

### 출력 

 <p>For each conversion problem, show the type of problem, its input string, and the converted result in the format shown below, replicating even the spacing exactly as shown. Leading zeroes are <u>not</u> allowed.</p>

