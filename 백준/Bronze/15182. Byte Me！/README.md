# [Bronze I] Byte Me! - 15182 

[문제 링크](https://www.acmicpc.net/problem/15182) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>Parity is an important concept in data transmission. Because the process is not error proof, parity is used to provide a check on whether or not data has been corrupted in transmission.</p>

<p>If even parity is being used, each byte will have an even number of 1 characters. If odd parity is being used, each byte will have an odd number of 1 characters.</p>

<p>In this problem, we are looking for a single bit that has been corrupted. To help you find it, the last byte is not part of the data being transmitted, but is a parity byte. Each bit of the parity byte will be used to make the corresponding bits in the data bytes odd or even depending on the parity being used.</p>

### 입력 

 <p>The first line of input is a single integer, N (3 <= N <= 10), the number of bytes of data to follow. The next N lines each contain a single byte of data consisting of 8 characters separated by spaces. Each character will be either 1 or 0. </p>

<p>There will be one further line of 8 characters (again 1 or 0) which will be the parity byte. In the parity byte, each bit is a parity bit for the corresponding bits in the preceding N lines, using the same parity as is used by the data bytes. The parity byte itself may not show the same parity as the data bytes.</p>

### 출력 

 <p>Output 3 lines of information about the data in the input. </p>

<ul>
	<li>Line 1: Either the word Even or the word Odd to describe the parity being used by the bytes which are not broken.</li>
	<li>Line 2: Byte is broken</li>
	<li>Line 3: Bit is broken</li>
</ul>

<p>is the number of the appropriate byte or bit, where the first of each is number 1.</p>

