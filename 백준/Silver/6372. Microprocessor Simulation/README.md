# [Silver III] Microprocessor Simulation - 6372 

[문제 링크](https://www.acmicpc.net/problem/6372) 

### 성능 요약

메모리: 109108 KB, 시간: 116 ms

### 분류

많은 조건 분기, 구현, 시뮬레이션

### 제출 일자

2024년 4월 7일 09:58:54

### 문제 설명

<p>Consider a small microprocessor that has the following properties:</p>

<ul>
	<li>Each word is four bits.</li>
	<li>Addresses are two words. The high word always comes first. That is, the high word of a two-word address will always occupy the lower word of memory.</li>
	<li>Memory is 256 words.</li>
	<li>There are two accumulators, A and B, each storing one word.</li>
	<li>There are nine instruction codes. Each instruction requires at least one word to store the code that specifies the instruction. Four instructions have arguments and require an additional two words.</li>
</ul>

<p>Each 4 bit number can have the values from 0 to 15, inclusive, in base 10. We will write these using hexadecimal in the usual way, i.e. A means 10, B means 11, etc.</p>

<p>These are the nine instructions:</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td style="text-align:center">Code</td>
			<td style="text-align:center">Words</td>
			<td>Description</td>
		</tr>
		<tr>
			<td style="text-align:center">0</td>
			<td style="text-align:center">3</td>
			<td>LD: Load accumulator A with the contents of memory at the specified argument.</td>
		</tr>
		<tr>
			<td style="text-align:center">1</td>
			<td style="text-align:center">3</td>
			<td>ST: Write the contents of accumulator A to the memory location specified by the argument.</td>
		</tr>
		<tr>
			<td style="text-align:center">2</td>
			<td style="text-align:center">1</td>
			<td>SWP: Swap the contents of accumulators A and B.</td>
		</tr>
		<tr>
			<td style="text-align:center">3</td>
			<td style="text-align:center">1</td>
			<td>ADD: Add the contents of accumulators A and B. The low word of the sum is stored in A, and the high word in B.</td>
		</tr>
		<tr>
			<td style="text-align:center">4</td>
			<td style="text-align:center">1</td>
			<td>INC: Increment accumulator A. Overflow is allowed; that is, incrementing F yields 0.</td>
		</tr>
		<tr>
			<td style="text-align:center">5</td>
			<td style="text-align:center">1</td>
			<td>DEC: Decrement accumulator A. Underflow is allowed; that is, decrementing 0 yields F.</td>
		</tr>
		<tr>
			<td style="text-align:center">6</td>
			<td style="text-align:center">3</td>
			<td>BZ: If accumulator A is zero, the next command to be executed is at the location specified by the argument. If A is not zero, the argument is ignored and nothing happens.</td>
		</tr>
		<tr>
			<td style="text-align:center">7</td>
			<td style="text-align:center">3</td>
			<td>BR: The next command to be executed is at the location specified by the argument.</td>
		</tr>
		<tr>
			<td style="text-align:center">8</td>
			<td style="text-align:center">1</td>
			<td>STP: Stop execution of the program.</td>
		</tr>
	</tbody>
</table>

<p> </p>

<p>The microprocessor always begins by executing the command at location 00. It executes the commands in sequence until it reaches the Stop command.</p>

<p>The examples below show partial programs and describe their affect.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td>Program</td>
			<td>Description</td>
		</tr>
		<tr>
			<td>01A8</td>
			<td>Load accumulator A with the contents of memory location 1A (26 in decimal) and stop.</td>
		</tr>
		<tr>
			<td>01A512F8</td>
			<td>Load accumulator A with the contents of memory location 1A (26 in decimal), decrement it, store the result to memory location 2F, then stop.</td>
		</tr>
	</tbody>
</table>

<p> </p>

### 입력 

 <p>The input will consist of several lines of exactly 256 hex characters. Each line is the contents of memory, beginning with address 00 and ending with address FF. The end of the input is indicated by a memory state that has a stop instruction (an “8”) at address 00. The input programs will never “fall of the end of memory”, that is, you will never execute an instruction that is located between addresses F0 and FF, inclusive.</p>

### 출력 

 <p>For each memory state, you should simulate execution beginning with address 00. When the stop instruction is reached, you will dump the contents of memory to the output as a single string of 256 hex characters followed by a newline character.</p>

<p> </p>

